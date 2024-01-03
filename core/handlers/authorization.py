import asyncio
from aiogram import Bot
from aiogram.types import Message
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='/Users/ovsa/Desktop/DIObot/.env')

# async def get_registration(message: Message, bot: Bot):

# async def get_authorize(message: Message, bot: Bot):


async def checkAdmin(message: Message, bot: Bot):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        msg = await message.answer(f'Вы авторизированны как администратор')

        # await
    else:
        msg = await message.answer(f'{message.from_user.first_name}, Вы авторизованы как участник')

    await message.delete()
    await asyncio.sleep(5)
    await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)