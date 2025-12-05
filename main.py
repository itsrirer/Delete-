import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

# =========================
#   ENVIRONMENT VARIABLES
# =========================
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

if not API_ID or not API_HASH or not BOT_TOKEN or not OWNER_ID:
    raise SystemExit("❌ Config Vars missing! Please set API_ID, API_HASH, BOT_TOKEN, OWNER_ID")

# =========================
#   BOT CLIENT
# =========================
bot = Client(
    "delete-all-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# =========================
#   DELETE ALL COMMAND
# =========================
@bot.on_message(filters.command("deleteallmessage") & filters.user(OWNER_ID))
async def delete_all_messages(client, message: Message):
    chat_id = message.chat.id

    status = await message.reply_text("🗑 Deleting all messages...\nPlease wait.")

    deleted = 0
    failed = 0
    batch = []
    BATCH_LIMIT = 100

    try:
        async for msg in client.get_chat_history(chat_id):
            batch.append(msg.id)

            # Delete in batches of 100
            if len(batch) >= BATCH_LIMIT:
                try:
                    await client.delete_messages(chat_id, batch)
                    deleted += len(batch)
                except:
                    # fallback — delete one by one
                    for mid in batch:
                        try:
                            await client.delete_messages(chat_id, mid)
                            deleted += 1
                        except:
                            failed += 1
                batch = []

        # Remaining messages
        if batch:
            try:
                await client.delete_messages(chat_id, batch)
                deleted += len(batch)
            except:
                for mid in batch:
                    try:
                        await client.delete_messages(chat_id, mid)
                        deleted += 1
                    except:
                        failed += 1

        await status.edit_text(
            f"✅ Done!\n"
            f"🗑 Deleted: {deleted}\n"
            f"⚠ Failed: {failed}"
        )

    except Exception as e:
        await status.edit_text(f"❌ Error: {e}")

# =========================
#   START BOT
# =========================
if __name__ == "__main__":
    print("🚀 Bot starting...")
    bot.run()
