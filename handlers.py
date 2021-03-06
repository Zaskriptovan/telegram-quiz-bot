from aiogram import types, Dispatcher

from database import db
import buttons
import quiz


async def send_welcome(message: types.Message):
    await message.answer('Привет! Готов проверить знания?', reply_markup=buttons.mainMenu)
    db.add_user(message.from_user.id, message.from_user.full_name)


async def start_game(message: types.Message):
    try:
        if message.text == 'Показать результат':
            await message.answer('Правильно ' + str(db.get_score(message.from_user.id)) + ' из 10',
                                 reply_markup=buttons.endMenu)

        elif message.text == 'Показать таблицу рекордов':
            await message.answer(db.get_table_records(), reply_markup=buttons.endMenu)

        elif message.text == 'Сыграть заново':
            await message.answer('Счет обнулён. Желаете сыграть еще раз?', db.reset_score(message.from_user.id),
                                 db.reset_index_question(message.from_user.id), reply_markup=buttons.mainMenu)

        elif message.text == 'Начать викторину':
            await message.answer(quiz.generate_question(message.from_user.id)['text'],
                                 reply_markup=quiz.generate_question(message.from_user.id)['keyboard'])

        elif message.text == quiz.get_correct_answer(message.from_user.id):
            db.update_score(message.from_user.id)
            db.update_index_question(message.from_user.id)
            await message.answer(quiz.generate_question(message.from_user.id)['text'],
                                 reply_markup=quiz.generate_question(message.from_user.id)['keyboard'])

        elif message.text in quiz.get_choices(message.from_user.id):
            db.update_index_question(message.from_user.id)
            await message.answer(quiz.generate_question(message.from_user.id)['text'],
                                 reply_markup=quiz.generate_question(message.from_user.id)['keyboard'])

        else:
            await message.answer('Нет такого варианта')

    except IndexError:
        await message.answer('Вы прошли викторину.', reply_markup=buttons.endMenu)


def register_handlers(disp: Dispatcher):
    disp.register_message_handler(send_welcome, commands=['start'])
    disp.register_message_handler(start_game)
