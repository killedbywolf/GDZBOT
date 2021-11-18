from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


'''---Main menu---'''

menu = ReplyKeyboardMarkup(
    [
     [
         KeyboardButton('Найти решение 🔎'), KeyboardButton('info ℹ')
     ]
    ],
    resize_keyboard=True
)

press_back = ReplyKeyboardMarkup(
    [
     [
         KeyboardButton('Вернуться в главное меню')
     ]
    ],
    resize_keyboard=True
)