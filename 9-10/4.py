import random

n = random.randint(1, 10)
u = None

while n != u:
    u = int(input('введи число'))

    if u == n:
        print('угадал!')
    else:
        print('не угадал')