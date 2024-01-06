# импорт библиотек, которые нужны будут для работоспособности бота
import asyncio
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


from core.handlers import games
from core.handlers import botCommands

load_dotenv(dotenv_path='/Users/ovsa/Desktop/DIObot/.env')


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(os.getenv('BOT_TOKEN'), parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(
        games.router,
        botCommands.router
    )

    try:
        # удаление ненужных обновлений
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
