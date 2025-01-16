import random

# 1
# a = input('Введи имя: ')
# b = input('Введи фамилию: ')
#
# print(f' {a} {b} - рады видеть вас в акадмеии')

#2

# r = int(input('радиус: '))
#
# if r < 0:
#     print('Неверные данные')
# else:
#     s = 3.14 * r**2
#     print(f'Площадь: {s}')

#3

# for i in range(100):
#     if i % 3 == 0:
#         print(i)
#
# for i in range(0, 100, 3):
#     print(i)


# 4
# s = 0
# for i in range(5):
#     price = int(input('Цена: '))
#     count = int(input('Количество: '))
#
#     if price > 0 and count > 0:
#         s = s + price * count
#     else:
#         print('неверные данные ')
#     print(s)


# 5

# question = input('Введи вопрос: ')
# num = random.randint(0, 1)
# if num == 0:
#     print('Нет...')
# else:
#     print('Да!')

# 6

# mark = int(input('Как ты отдохнул от 1 до 10?'))
#
# if mark < 0 or mark > 10:
#     print('неверные данные')
# elif mark >= 8 and mark <= 10:
#     print('здорово!  Вы хорошо отдохнули')
# elif mark >= 6:
#     print('неплохой результат')
# elif mark >= 4:
#     print(' вам бы еще недельку, да? ')
# elif mark >0:
#     print(' бывает, все впереди. ')

# 7

# ans = input('Угадай подарок?')
#
# res = 'машина'
#
# while ans != res:
#     ans = input('Угадай подарок?')
#
# print('угадал')

# ans = ''
# res = 'машина'
#
# while ans != res:
#     ans = input('Угадай подарок?')
#
# print('угадал')


# 8

while True:
    rub = int(input('Введи сумму: '))
    val = input('Введи, во что первести. 1 - доллар, 2 - евро, 3 - юани, 4 - выход')

    if val == '1':
        print(rub/102)
    elif val == '2':
        print(rub / 107)
    elif val == '3':
        print(rub / 14)
    elif val == '4':
        break