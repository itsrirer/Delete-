import os
from pyrogram import Client, filters
from pyrogram.types import Message

# =========================
# CONFIG (ENV VARIABLES)
# =========================
API_ID = int(os.getenv("API_ID", "29544631"))
API_HASH = os.getenv("API_HASH", "e37dea5444dd48fd626d9a91fa13487b")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8595992416:AAHg7vmU9OlUt0TZLLcD7pzqf1_L_mZk-uo")
OWNER_ID = [int(os.getenv("OWNER_ID", "6127154811"))]

# =========================
# BOT CLIENT
# =========================
app = Client(
    "delete-all-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# =========================
# DELETE ALL MESSAGES IN GROUP
# =========================
@app.on_message(filters.group)
async def delete_all(client, message: Message):
    try:
        await message.delete()
    except:
        pass

# =========================
# ALIVE CHECK (PRIVATE TO OWNER)
# =========================
@app.on_message(filters.private & filters.user(OWNER_ID))
async def alive(client, message: Message):
    await message.reply("✅ Bot is Running Successfully!")

# =========================
# START BOT
# =========================
print("🚀 Bot Started... Heroku Worker Active")
app.run()
