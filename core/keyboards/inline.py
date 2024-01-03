from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text='TG',
                   url=f'tg://user?id=441557434',
                   callback_data='')
    builder.button(text='TG', url='tg://user?id=441557434')
    builder.button(text='TG', url='tg://user?id=441557434')
    builder.adjust(1, 2, repeat=True)
    return builder.as_markup()

