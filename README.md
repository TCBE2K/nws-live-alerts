# nws-live-alerts
A Python program that checks the NWS API every minute and sends an HTTP request when a new alert comes out.

## Setup

1. Install dependencies using the requirements.txt file, with the command `pip install -r requirements.txt`
2. Create .env file (and add your variables):
   ```
   LATITUDE=
   LONGITUDE=
   TELEGRAM_BOT_TOKEN=
   TELEGRAM_CHAT_ID=
   ```
4. Start the Python script

This will use the Telegram API to send a message to your specified chat id using the bot token.
