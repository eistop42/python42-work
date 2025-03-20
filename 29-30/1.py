number1 = int(input('Введи первое число'))
number2 = int(input('Введи второе число'))

action = input('Введи: +/*-')

if action == '+':
    print(number1+number2)
elif action == '-':
    print(number1-number2)
elif action == '*':
    print(number1*number2)
elif action == '/':
    print(number1/number2)