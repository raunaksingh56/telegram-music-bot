from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
import random

suggestions = [
    "Coldplay – Viva La Vida",
    "Imagine Dragons – Believer",
    "Ed Sheeran – Shape of You",
    "Lo-fi Chill Beats",
    "Hans Zimmer – Time",
    "Adele – Easy On Me"
]

async def suggest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sample = random.sample(suggestions, 3)
    await update.message.reply_text("🎧 Suggested Tracks:\n" + "\n".join(f"• {s}" for s in sample))

suggest_handler = CommandHandler("suggest", suggest)
