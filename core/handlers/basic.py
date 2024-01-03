from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.inline import get_inline_keyboard


async def get_start(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Приветствую тебя, {message.from_user.first_name}')
    await message.delete()


async def get_help(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"{message.from_user.id}")
    await message.delete()
    print(json.dumps(message.model_dump(), default=str))


async def get_inline(message: Message):
    await message.answer(text='ссылки',
                         reply_markup=get_inline_keyboard())
    await message.delete()
