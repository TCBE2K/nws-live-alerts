# nws-live-alerts
A Python program that checks the NWS API every minute and sends an HTTP request when a new alert comes out.

## Setup

1. Install dependencies using the requirements.txt file, with the command `pip install -r requirements.txt`
2. Change variables on lines 26 to 30.
3. Start the Python script

By default, this will use the Telegram API to send a message in a chat, however you can modify the script to set it to something else, like a Discord webhook.
