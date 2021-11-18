from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

subjects_menu_10 = InlineKeyboardMarkup(row_width=1)
subjects = {  # Ключ - название предмета, значение - callback
    'Алгебра': 'algebra_for_10',
    'Геометрия': 'geometry_for_10',
    'Английский язык': 'eng_for_10',
    'Физика': 'physics_for_10',
    'Химия': 'chemistry_for_10'
}

'''------Inline-кнопки предметов для 10 класса------ '''

for name, callback in subjects.items():
    button_subjects = InlineKeyboardButton(text=name, callback_data=callback)
    subjects_menu_10.insert(button_subjects)

button_back_to_classes = InlineKeyboardButton(text='Назад', callback_data='press_back_classes')
subjects_menu_10.insert(button_back_to_classes)
