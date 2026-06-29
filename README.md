============================================================
OmniStat Tracker v1.0 - Setup & Installation Guide
============================================================

Thank you for your purchase! Follow these simple steps to 
get your premium live statistics tracker up and running.

Step 1: Install Dependencies
-----------------------------
Make sure you have Python installed on your server environment.
Open your terminal panel and run:
pip install -r requirements.txt

Step 2: Add Your Bot Token & Target IP
---------------------------------------
1. Open the "config.json" file.
2. Change the "MINECRAFT_SERVER_IP" value to your server's IP address.
3. Look for your host panel's Environment Variables panel.
4. Add a new key named: DISCORD_TOKEN
5. Paste your Discord Bot Token as the value.

Step 3: Run the Bot
--------------------
Start the application using:
python main.py

The bot will automatically connect and update its activity status profile 
with real-time player data counts every 60 seconds!
