from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def reply_keyboards():
    builder = ReplyKeyboardBuilder()
    builder.button(text='Войти в аккаунт')
    builder.button(text='Зарегистрироваться')
    return builder.as_markup(resize_keyboard=True)
