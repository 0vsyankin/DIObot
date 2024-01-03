from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text='TG',
                   url=f'tg://user?id=441557434',
                   callback_data='')
    builder.adjust(repeat=True)
    return builder.as_markup()
