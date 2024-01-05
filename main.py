# импорт библиотек, которые нужны будут для работоспособности бота
import asyncio
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv(dotenv_path='/Users/ovsa/Desktop/DIObot/.env')


async def start_bot():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()

    dp.include_routers(

    )

    try:
        # удаление ненужных обновлений
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start_bot())
