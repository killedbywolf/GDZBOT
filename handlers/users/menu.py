from aiogram.dispatcher.filters import Command, Text
from keybourds import menu
from aiogram.types import Message
from loader import dp


@dp.message_handler(Command('start'))
async def main_menu(message: Message):
    await message.answer('Главное меню', reply_markup=menu)


@dp.message_handler(Text('info ℹ'))
async def main_menu(message: Message):
    await message.answer('Бот является авторским фан-проектом')


@dp.message_handler(Text('Вернуться в главное меню'))
async def main_menu(message: Message):
    await message.answer('Главное меню', reply_markup=menu)
