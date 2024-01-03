import asyncio
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from core.handlers.basic import get_start, get_help, get_inline

load_dotenv()


async def start_bot(bot: Bot):
    await bot.send_message(os.getenv('ADMIN_ID'), text='запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(os.getenv('ADMIN_ID'), text='остановлен')


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(get_help, Command(commands=['help']))
    dp.message.register(get_inline, Command(commands=['inline']))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
