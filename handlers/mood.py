from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

mood_library = {
    "relax": ["Lo-fi chill", "Soft piano"],
    "study": ["Ambient focus", "Instrumental beats"],
    "party": ["EDM hits", "Top 40"],
    "sad": ["Emotional piano", "Slow acoustic"]
}

async def mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("🎭 Use: /mood relax | study | sad | party")
        return

    mood_type = context.args[0].lower()
    songs = mood_library.get(mood_type)

    if songs:
        await update.message.reply_text(
            f"🎶 {mood_type.title()} suggestions:\n" +
            "\n".join(f"• {s}" for s in songs)
        )
    else:
        await update.message.reply_text("❌ Unknown mood. Try: relax, study, sad, party")

mood_handler = CommandHandler("mood", mood)
