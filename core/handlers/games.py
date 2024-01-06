import random
import asyncio

from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram.enums import DiceEmoji

router = Router()


@router.message(Command(commands=["rn", "random_number"]))
async def get_random_number(message: Message, command: CommandObject):
    a, b = [int(n) for n in command.args.split("-")]
    random_num = random.randint(a, b)
    await message.reply(f'Random number between {a} and {b} is {random_num}')


@router.message(F.text == 'play')
async def game_six(message: Message):
    x = await message.answer_dice(DiceEmoji.DICE)

    n = [1, 2, 3, 4, 5]
    print(x.dice.value)

    if x.dice.value in n and x.dice.value <= 3:
        a = await message.answer(f'Вам выпало {x.dice.value}, ничего страшного! Попробуйте ещё раз!')
    elif x.dice.value in n and x.dice.value <= 5:
        a = await message.answer(f'Вам выпало {x.dice.value}, уже лучше! Попробуйте ещё раз!')
    else:
        a = await message.answer(f'Поздравляю Вам выпало {x.dice.value}! До новых встреч!')
    await asyncio.sleep(3)

