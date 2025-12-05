from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import os

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

bot = Client(
    "deleteall-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("deleteallmessage") & filters.user(OWNER_ID))
async def delete_all(_, msg: Message):
    chat_id = msg.chat.id
    await msg.reply("🗑 Deleting all messages...")

    deleted = 0
    failed = 0
    batch = []
    BATCH_SIZE = 100

    try:
        async for message in bot.get_chat_history(chat_id):
            batch.append(message.id)

            if len(batch) >= BATCH_SIZE:
                try:
                    await bot.delete_messages(chat_id, batch)
                    deleted += len(batch)
                except:
                    for mid in batch:
                        try:
                            await bot.delete_messages(chat_id, mid)
                            deleted += 1
                        except:
                            failed += 1
                batch = []

        if batch:
            try:
                await bot.delete_messages(chat_id, batch)
                deleted += len(batch)
            except:
                for mid in batch:
                    try:
                        await bot.delete_messages(chat_id, mid)
                        deleted += 1
                    except:
                        failed += 1

        await bot.send_message(chat_id, f"✅ Done!\nDeleted: {deleted}\nFailed: {failed}")

    except Exception as e:
        await msg.reply(f"Error: {e}")

bot.run()
