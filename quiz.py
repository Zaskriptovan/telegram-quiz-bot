from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from database import db
from questions import questions


def get_text_question(user_id):
    index_question = db.get_index_question(user_id)
    list_ques = list(questions)
    text_ques = list_ques[index_question]

    return text_ques


def get_correct_answer(user_id):
    correct_answer = questions[get_text_question(user_id)][0]
    return correct_answer


def get_choices(user_id):
    choices = questions[get_text_question(user_id)][1]
    return choices


def generate_question(user_id):
    keyboard = ReplyKeyboardMarkup()
    for i in get_choices(user_id):
        keyboard.row(KeyboardButton(i))

    return {'text': get_text_question(user_id), 'keyboard': keyboard}
