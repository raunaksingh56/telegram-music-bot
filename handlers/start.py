from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎧 Welcome to Music Bot!\n"
        "Commands:\n"
        "/play <song> - Download and play music\n"
        "/mood <type> - Music by mood\n"
        "/suggest - Get random suggestions\n"
        "/history - Show your last 5 songs"
    )

start_handler = CommandHandler("start", start)
