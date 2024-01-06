import asyncio

from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command

from core.keyboards.reply import reply_keyboards

router = Router()


@router.message(Command("start"))
async def start(message: Message, bot: Bot):
    start_msg = await message.answer(f'Привет, <tg-spoiler>{message.from_user.username}</tg-spoiler>',
                                     reply_markup=reply_keyboards())

    await message.delete()
    await asyncio.sleep(25)

    await bot.delete_message(chat_id=start_msg.chat.id, message_id=start_msg.message_id)

# @router.message(F.text == 'Зарегистрироваться')
# async def cmd_registration(message: Message, bot: Bot)
