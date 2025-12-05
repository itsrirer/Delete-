# Telegram Delete-All Bot

## Commands:
/deleteallmessage → Deletes all messages in the chat (Owner Only)

## Setup (Heroku)
1. Set config vars:
   - API_ID
   - API_HASH
   - BOT_TOKEN
   - OWNER_ID

2. Add buildpack:
   heroku/python

3. Deploy and turn ON worker dyno.

## Run Locally:
export API_ID=123
export API_HASH="abc"
export BOT_TOKEN="bot_token"
export OWNER_ID=123456
pip install -r requirements.txt
python main.py
