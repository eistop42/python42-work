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

import time
# задание 1
# for user in users:
#     time.sleep(2)
#     print(user['name'], user['balance'])
#     print(f'{user['name']} -- {user['balance']}')

# задание 2
# for user in users:
#     if user['name'] == 'Сергей':
#         print(user['name'], user['balance'])
#         # print(f'{user['name']} -- {user['balance']}')


# задание 3

# for user in users:
#     if user['balance'] > 2000:
#         print(user['name'], user['balance'])


# задание 4

# sum = 0
#
# for user in users:
#     sum = sum + user['balance']
#
# print(sum)

# задание 5

# for user in users:
#     b = int(user['balance'] * 1.1)
#     user['balance'] = b
# print(users)


# задание 6

min_b = users[0]
max_b = users[0]

for user in users:
    if user['balance'] < min_b['balance']:
        min_b = user
    if user['balance'] > max_b['balance']:
        max_b = user

print(min_b)
print(max_b)