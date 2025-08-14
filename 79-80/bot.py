import telebot

# импорт переменной с базой данных
from database import db

token = ''
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def hello(message):
    # добавляем пользователя
    first_name = message.chat.first_name
    telegram_id  = message.chat.id
    # добавляем только, если нет
    if not db.get_user_by_id(telegram_id):
        db.add_user(telegram_id, first_name)

    bot.send_message(message.chat.id, f'Привет, {first_name}!')

@bot.message_handler(commands=['costs'])
def costs(message):
    costs = db.get_costs()

    for cost in costs:
        row = f'{cost[0]}:{cost[1]}'
        bot.send_message(message.chat.id, row)


@bot.message_handler(commands=['add'])
def add(message):
    # достаем траты из базы
    bot.send_message(message.chat.id, 'Введи название товара: ')
    # ввод пользователя будет обрабатываться функцией save_name
    bot.register_next_step_handler(message, save_name)

def save_name(message):
    """Запомнили имя, пепедали в следующий обработчик"""
    name = message.text
    bot.send_message(message.chat.id, 'Введи стоимость: ')
    bot.register_next_step_handler(message, save_price, name)

def save_price(message, name):
    # запись товара в базу данных
    price = message.text
    db.add_cost(name, price)

bot.infinity_polling()


