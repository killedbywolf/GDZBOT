from loader import dp
from aiogram.types import CallbackQuery
from keybourds import classes_menu, subjects_menu_10


@dp.callback_query_handler(text='10 <-class')
async def show_subjects(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer('Выберите предмет', reply_markup=subjects_menu_10)


@dp.callback_query_handler(text='11 <-class')
async def show_subjects(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer('Раздел находиться в разработке;)')


@dp.callback_query_handler(text='press_back_classes')
async def back_to_classes(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer('Выберите класс', reply_markup=classes_menu)

