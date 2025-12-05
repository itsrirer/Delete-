import os
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "").split()))

app = Client(
    "delete-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Only Delete Messages Bot

@app.on_message(filters.group)
async def delete_all(client, message: Message):
    try:
        await message.delete()
    except:
        pass


@app.on_message(filters.private & filters.user(OWNER_ID))
async def alive(client, message: Message):
    await message.reply("Bot Running Successfully ✔️")


print("Bot Started Successfully...")
app.run()
