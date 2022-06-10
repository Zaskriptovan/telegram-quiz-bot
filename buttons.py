from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ---------Main Menu--------------
buttonStartQuiz = KeyboardButton('Начать викторину')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonStartQuiz)

# ---------End menu--------------
buttonResult = KeyboardButton('Показать результат')
buttonTableRecords = KeyboardButton('Показать таблицу рекордов')
buttonResetScore = KeyboardButton('Сыграть заново')
endMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonResult).add(
    buttonTableRecords).add(buttonResetScore)
