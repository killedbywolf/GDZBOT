from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

'''------------Выбор класса-------------'''

classes_menu = InlineKeyboardMarkup(row_width=2)

for _ in range(10, 12):
    button_class = InlineKeyboardButton(text=str(_) + ' класс', callback_data=str(_) + ' <-class')
    classes_menu.insert(button_class)
