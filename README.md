# Delete-All Bot (Heroku / Telegram)

This bot deletes all messages in groups automatically. Only Owner can check alive.

## Setup (Heroku)

1. Set Config Vars:
   - API_ID = 29544631
   - API_HASH = e37dea5444dd48fd626d9a91fa13487b
   - BOT_TOKEN = 8595992416:AAHg7vmU9OlUt0TZLLcD7pzqf1_L_mZk-uo
   - OWNER_ID = 6127154811

2. Add Buildpack:
   heroku/python

3. Deploy and turn ON worker dyno.

## Run Locally
export API_ID=29544631
export API_HASH=e37dea5444dd48fd626d9a91fa13487b
export BOT_TOKEN=8595992416:AAHg7vmU9OlUt0TZLLcD7pzqf1_L_mZk-uo
export OWNER_ID=6127154811

pip install -r requirements.txt
python main.py
