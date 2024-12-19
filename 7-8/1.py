import random


number = random.randint(1, 10)

for i in range(5):
    user = int(input('угадай число: '))

    if number < user:
        print('Надо меньше')
    elif number > user :
        print('Надо больше')
    else:
        print('Угадал 😎')
        break



