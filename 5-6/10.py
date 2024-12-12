import random

number = int(input('введи число: '))

comp = random.randint(1, 10)

if number < comp:
    print('нужно больше')
elif number > comp:
    print('нужно меньше')
elif number == comp:
    print('угадал')