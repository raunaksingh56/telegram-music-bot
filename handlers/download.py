from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.downloader import download_song
from utils.database import add_song_to_history

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Please provide a song name.")
        return

    query = " ".join(context.args)
    await update.message.reply_text(f"🔎 Searching: {query}")
    file_path, title = download_song(query)

    if file_path:
        add_song_to_history(update.effective_user.id, title)
        await update.message.reply_audio(audio=open(file_path, 'rb'), title=title)
    else:
        await update.message.reply_text("❌ Couldn't download that song.")

download_handler = CommandHandler("play", play)
