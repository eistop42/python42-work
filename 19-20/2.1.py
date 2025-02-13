users = [
    {"id": 1, "name": "Алексей", "balance": 1500},
    {"id": 2, "name": "Марина", "balance": 2300},
    {"id": 3, "name": "Иван", "balance": 500},
    {"id": 4, "name": "Ольга", "balance": 3200},
    {"id": 5, "name": "Дмитрий", "balance": 1750},
    {"id": 6, "name": "Екатерина", "balance": 800},
    {"id": 7, "name": "Сергей", "balance": 4200},
    {"id": 8, "name": "Наталья", "balance": 1200},
    {"id": 9, "name": "Владимир", "balance": 2900},
    {"id": 10, "name": "Анна", "balance": 3400},
]


id_from = input('От кого отправляем')
id_to = input('Кому отправляем')
amount = input('Сколько отправляем')

user_from = None
user_to = None

# ищем отправителя и получателя
for user in users:
    if user['id'] == int(id_from):
        user_from = user
    if user['id'] == int(id_to):
        user_to = user


if user_to and user_from:

    user_from['balance'] = user_from['balance'] - int(amount)
    user_to['balance'] = user_to['balance'] + int(amount)
else:
    print('неверный id')

print(users)

