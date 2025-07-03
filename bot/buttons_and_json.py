import os.path

import telebot
import json
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

token = ''

bot = telebot.TeleBot(token)

# сохранить базу
def save_db(users):
    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False)

# прочитать базу
def get_db():
    if os.path.exists('users.json'):
        with open('users.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

@bot.message_handler(commands=['start'])
def hello(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("сказать привет"), KeyboardButton("помощь"), KeyboardButton("регистрация"))

    bot.send_message(message.chat.id, 'Привет, чем помочь?', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'сказать привет')
def button_hello(message):
    bot.reply_to(message, 'привет!!!')

@bot.message_handler(func=lambda message: message.text == 'регистрация')
def button_hello(message):
    bot.reply_to(message, 'Введи имя: ')
    bot.register_next_step_handler(message, save_user_name)

def save_user_name(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Пока'))
    bot.send_message(message.chat.id, 'Сохранил в базу', reply_markup=markup)

    # читаем базу
    users = get_db()
    # добавить пользователя в словарь users
    user_id = message.chat.id
    name = message.text
    users.update({user_id: {'name': name}})

    # сохраняем
    save_db(users)
    print(users)


bot.infinity_polling()