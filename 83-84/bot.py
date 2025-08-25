import telebot
import re

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from db import db
token = ''

bot = telebot.TeleBot(token)


def get_next_question(current=0):
    """Возвращает следующий вопрос и варианты ответов в виде инлайн кнопок"""
    question = db.get_next_question(current)

    markup = InlineKeyboardMarkup()
    if question:
        answers = db.get_answers(question.id)
        for answer in answers:
            markup.add(InlineKeyboardButton(text=answer.text, callback_data=f'question_id={question.id}&answer_id={answer.id}'))

    return question, markup


@bot.message_handler(commands=['start'])
def start(message):
    """Приветствие и отправка первого вопроса"""
    question, markup = get_next_question()

    bot.send_message(message.chat.id, 'Начинаем викторину')
    bot.send_message(message.chat.id, question.text, reply_markup=markup)

def filter_answers(callback):
    data = callback.data
    res = re.search(r'^question_id=\d+', data)
    return res

@bot.callback_query_handler(func=filter_answers)
def check_answer(callback):
    data = callback.data
    # получаем значения параметров question_id и answer_id в формате (12, 2)
    res = re.findall(r'question_id=(\d+)&answer_id=(\d+)', data)[0]
    # присваиваем значения переменным
    question_id = int(res[0])
    answer_id = int(res[1])

    check_answer = db.check_answer(question_id, answer_id)
    print(check_answer)
    if check_answer:
        bot.send_message(callback.message.chat.id, 'Правильно!')
    else:
        bot.send_message(callback.message.chat.id, 'Не правильно')
    # получили следующий вопрос
    question, markup = get_next_question(question_id)
    # задаем следующий вопрос
    if question:
        bot.send_message(callback.message.chat.id, question.text, reply_markup=markup)
    else:
        bot.send_message(callback.message.chat.id, 'конец викторины')

bot.infinity_polling()