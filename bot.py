from telegram.ext import ApplicationBuilder
from handlers.start import start_handler
from handlers.download import download_handler
from handlers.mood import mood_handler
from handlers.suggest import suggest_handler
from handlers.history import history_handler
import config

app = ApplicationBuilder().token(config.BOT_TOKEN).build()

app.add_handler(start_handler)
app.add_handler(download_handler)
app.add_handler(mood_handler)
app.add_handler(suggest_handler)
app.add_handler(history_handler)

print("✅ Bot is running...")
app.run_polling()
