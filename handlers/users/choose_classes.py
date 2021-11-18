from loader import dp
from aiogram.types import Message
from keybourds.inline import classes_menu
from keybourds.default import press_back
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text('Найти решение 🔎'))
async def show(message: Message):
    await message.answer('...', reply_markup=press_back)
    await message.answer('Выберите класс', reply_markup=classes_menu)

