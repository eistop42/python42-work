import telebot
import random

token = ''

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def hello(message):
    bot.reply_to(message, 'Привет, чем помочь?')

@bot.message_handler(commands=['game'])
def game(message):
    bot.reply_to(message, 'Начинаем игру! Отгадай число от 1 до 10')

@bot.message_handler(func=lambda m:True)
def check_number(message):
    comp = random.randint(1, 10)
    user = int(message.text)
    if comp == user:
        bot.reply_to(message, f'Угадал!😎😎😎')
    else:
        bot.reply_to(message, f'Не правильно 😐 было {comp}')


bot.infinity_polling()