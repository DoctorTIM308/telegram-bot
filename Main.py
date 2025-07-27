import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

logging.basicConfig(level=logging.INFO)

# Tokenni .env dan olishga harakat qilamiz
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Siz murojaat botidasiz.")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Xabaringiz qabul qilindi. Rahmat!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
