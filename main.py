import discord
from discord.ext import tasks, commands
import os
import json

if os.path.exists("config.json"):
    with open("config.json", "r") as f:
        config = json.load(f)
else:
    config = {"MINECRAFT_SERVER_IP": "2b2t.org", "UPDATE_INTERVAL_SECONDS": 60}

class StatBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = False  
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        self.update_status_loop.start()

    @tasks.loop(seconds=config.get("UPDATE_INTERVAL_SECONDS", 60))
    async def update_status_loop(self):
        server_ip = os.getenv("MINECRAFT_SERVER_IP", config.get("MINECRAFT_SERVER_IP", "2b2t.org"))
        try:
            from mcstatus import MCServer
            server = MCServer.lookup(server_ip)
            status = await server.async_status()
            status_text = f"🎮 {status.players.online}/{status.players.max} players on {server_ip}"
            await self.change_presence(activity=discord.Game(name=status_text))
        except Exception as e:
            await self.change_presence(activity=discord.Game(name="⚠️ Server Offline"))

    @update_status_loop.before_loop
    async def before_update_loop(self):
        await self.wait_until_ready()

bot = StatBot()

@bot.event
async def on_ready():
    print(f"🤖 Operational Status: Online as {bot.user.name}")

if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if token:
        bot.run(token)
    else:
        print("❌ CRITICAL ERROR: Environment variable 'DISCORD_TOKEN' missing.")
