number1 = int(input('Первое число:'))
number2 = int(input('Второе число:'))
action = input('Действие: +/-*')

if action == '+':
    print(number1 + number2)
elif action == '-':
    print(number1 - number2)
elif action == '*':
    print(number1 * number2)
elif action == '/':
    print(number1 / number2)
else:
    print('не то действие')