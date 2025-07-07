import telebot

from yandex import YandexGPT
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

yandex = YandexGPT()

token = ''
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(KeyboardButton('Задать вопрос'))

    inline_markup = InlineKeyboardMarkup()
    inline_markup.add(InlineKeyboardButton(text='Задать вопрос', callback_data='ask_question'))
    bot.send_message(message.chat.id, 'Привет, выбирай', reply_markup=inline_markup)

@bot.message_handler(func=lambda message: message.text == 'Задать вопрос')
def ask_question(message):
    bot.send_message(message.chat.id, 'Задавай свой вопрос: ', reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, get_answer)

@bot.callback_query_handler(func=lambda callback: callback.data == 'ask_question')
def test_inline(callback):
    message = callback.message

    inline_markup = InlineKeyboardMarkup()
    inline_markup.add(InlineKeyboardButton(text='философ', callback_data='phil'))
    inline_markup.add(InlineKeyboardButton(text='друг', callback_data='friend'))

    bot.edit_message_text( 'задвай вопрос нейросети', message.chat.id, message.id, reply_markup=inline_markup)
    bot.register_next_step_handler(message, get_answer)

def get_answer(message):
    if message.text == '/cancel':
        return bot.reply_to(message, 'вышел из диалога')
    text = message.text
    answer = yandex.get_answer(text)
    bot.reply_to(message, answer)
    bot.register_next_step_handler(message, get_answer)



bot.infinity_polling()