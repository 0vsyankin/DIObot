# импорт библиотек, которые нужны будут для работоспособности бота
import asyncio
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(F.text == '/start')
async def start(message: Message):
    start_msg = await message.answer(f'Привет, <tg-spoiler>{message.from_user.username}</tg-spoiler>')
    await message.delete()
    await asyncio.sleep(15)
    await bot.delete_message(chat_id=start_msg.chat.id, message_id=start_msg.message_id)


async def main():
    # logging.basicConfig(level=logging.INFO)

    try:
        # удаление ненужных обновлений
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
