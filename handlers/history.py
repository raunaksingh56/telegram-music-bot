from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.database import get_last_songs

async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    songs = get_last_songs(user_id)

    if songs:
        await update.message.reply_text(
            "🕘 Last Played:\n" + "\n".join(f"• {s}" for s in songs)
        )
    else:
        await update.message.reply_text("🔍 No history found.")

history_handler = CommandHandler("history", history)
