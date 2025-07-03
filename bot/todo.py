import os.path

import telebot
import json
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

token = '7787720175:AAEikqHLBCSI8vWL3mN7bDXnuw7MA2VDxTQ'

bot = telebot.TeleBot(token)


def load_db():
    if not os.path.exists('users.json'):
        return {}
    with open('users.json', encoding='utf-8') as f:
        return json.load(f)

def save_db(users):
    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False)

@bot.message_handler(commands=['start'])
def hello(message):
    markup = ReplyKeyboardMarkup()
    markup.add(KeyboardButton('Добавить дело'), KeyboardButton('Посмотреть дела'))
    bot.send_message(message.chat.id, 'Привет, чем помочь?', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Добавить дело')
def ask_todo(message):
    bot.reply_to(message, 'Напиши текcт: ')
    bot.register_next_step_handler(message, save_todo)

def save_todo(message):
    users = load_db()
    user_id = str(message.chat.id)
    if user_id not in users:
        users[user_id] = {'tasks': [message.text]}
    else:
        users[user_id]['tasks'].append(message.text)
    save_db(users)
    bot.reply_to(message, 'сохранил')
    print(users)


@bot.message_handler(func=lambda message: message.text == 'Посмотреть дела')
def show_todo(message):
    users = load_db()
    user_id = str(message.chat.id)
    if  str(message.chat.id) not in users:
        bot.reply_to(message, 'задач нет')
    else:
        tasks = users[user_id]['tasks']
        numbered_tasks = []
        for number, task in enumerate(tasks, start=1):
            numbered_tasks.append(f'{number}.{task}')
        tasks = "\n".join(numbered_tasks)
        bot.reply_to(message, tasks)

bot.infinity_polling()