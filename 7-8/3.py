number1 = int(input('число 1 '))
number2 = int(input('число 2 '))

for i in range(number1,number2 ):
    if i % 2 != 0:
        print(f'Число нечетное: {i}')