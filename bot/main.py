import os

from dotenv import load_dotenv
from telegram import Bot
from telegram.ext import Updater, MessageHandler, filters, ApplicationBuilder

from .handlers import decode_qr_handler

load_dotenv()

START_ROUTES, END_ROUTES = range(2)

def start_bot():
    # bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
    application = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
    # updater = Updater(token=os.getenv("TELEGRAM_TOKEN"))
    application.add_handler(MessageHandler(filters.TEXT, decode_qr_handler))
    application.run_polling()


