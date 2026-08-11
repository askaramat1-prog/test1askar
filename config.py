from aiogram import Bot, Dispatcher
from decouple import config

BOT_TOKEN = config("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
