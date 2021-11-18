from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

authors_menu_algebra_10 = InlineKeyboardMarkup(row_width=1)
authors_menu_geometry_10 = InlineKeyboardMarkup(row_width=1)
authors_menu_eng_10 = InlineKeyboardMarkup(row_width=1)
authors_menu_physics_10 = InlineKeyboardMarkup(row_width=1)
authors_menu_chemistry_10 = InlineKeyboardMarkup(row_width=1)

algebra_authors = {
    'Никольский С.М., Потапов М.К., Решетников Н.Н': 'algebra_NPR_10'
}
geometry_authors = {
    'Атанасян Л.С., Бутузов В.Ф., Кадомцев С.Б.': 'geometry_ABK_10'
}
eng_authors = {
    'В. Эванс, Д. Дули, О.В. Афанасьева': 'eng_ADA_10'
}
physics = {
    'Г.Я. Мякишев, Б.Б. Буховцев, Н.Н. Сотский': 'physics_MBS_10'
}
chemistry = {
    'О.С. Габриелян': 'chemistry_G_10'
}

for authors, callback in algebra_authors.items():  # Создаем кнопки с авторами учебников по алгебре
    algebra_button = InlineKeyboardButton(text=authors, callback_data=callback)
    authors_menu_algebra_10.insert(algebra_button)

for authors, callback in geometry_authors.items():  # Создаем кнопки с авторами учебников по геометрии
    geometry_button = InlineKeyboardButton(text=authors, callback_data=callback)
    authors_menu_geometry_10.insert(geometry_button)

for authors, callback in eng_authors.items():  # Создаем кнопки с авторами учебников по английскому языку
    eng_button = InlineKeyboardButton(text=authors, callback_data=callback)
    authors_menu_eng_10.insert(eng_button)

for authors, callback in physics.items():  # Создаем кнопки с авторами учебников по физике
    physics_button = InlineKeyboardButton(text=authors, callback_data=callback)
    authors_menu_physics_10.insert(physics_button)

for authors, callback in chemistry.items():  # Создаем кнопки с авторами учебников по химии
    chemistry_button = InlineKeyboardButton(text=authors, callback_data=callback)
    authors_menu_chemistry_10.insert(chemistry_button)


button_back_to_subjects = InlineKeyboardButton(text='Назад', callback_data='press_back_subjects') # Кнопка 'Назад'
for authors_menu in (authors_menu_algebra_10, authors_menu_geometry_10,
                     authors_menu_eng_10, authors_menu_physics_10,
                     authors_menu_chemistry_10
                     ):
    authors_menu.insert(button_back_to_subjects)
