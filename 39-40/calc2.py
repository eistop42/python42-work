
def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

count = 0
while True:
    number1 = int(input('Первое число:'))
    number2 = int(input('Второе число:'))
    action = input('Действие: +/-*')

    if action == '+':
        res = add(number1, number2)
        print(res)
        count += 1
    elif action == '-':
        print(subtract(number1, number2))
        count += 1
    elif action == '*':
        print(multiply(number1, number2))
        count += 1
    elif action == '/':
        print(divide(number1, number2))
        count += 1
    elif action == 'q':
        break
    else:
        print('не то действие')

print(f'Кол-во операций: {count}')