from loader import dp
from aiogram.types import CallbackQuery
from keybourds.inline.all_for_10 import *


@dp.callback_query_handler(text='algebra_for_10')
async def show_authors_algebra(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer('Выберите автора', reply_markup=authors_menu_algebra_10)


@dp.callback_query_handler(text='geometry_for_10')
async def show_authors_algebra(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer('Выберите автора', reply_markup=authors_menu_geometry_10)


@dp.callback_query_handler(text='eng_for_10')
async def show_authors_algebra(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer('Выберите автора', reply_markup=authors_menu_eng_10)


@dp.callback_query_handler(text='physics_for_10')
async def show_authors_algebra(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer('Выберите автора', reply_markup=authors_menu_physics_10)


@dp.callback_query_handler(text='chemistry_for_10')
async def show_authors_algebra(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer('Выберите автора', reply_markup=authors_menu_chemistry_10)


@dp.callback_query_handler(text='press_back_subjects')
async def back_to_subjects(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer('Выберите предмет', reply_markup=subjects_menu_10)