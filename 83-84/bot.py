import telebot

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from db import db
token = ''

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    """Приветствие и отправка первого вопроса"""
    question = db.get_next_question()
    answers = db.get_answers(question.id)

    markup = InlineKeyboardMarkup()
    for answer in answers:
        markup.add(InlineKeyboardButton(text=answer.text, callback_data=answer.text))

    bot.send_message(message.chat.id, 'Начинаем викторину')
    bot.send_message(message.chat.id, question.text, reply_markup=markup)

bot.infinity_polling()