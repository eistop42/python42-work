number_1 = int(input('первое число: '))
number_2 = int(input('второе число: '))

action = input('1 - сложить, 2 - умножить')


def sum_numbers(a, b):
    return a+b


if action == '1':
    print(sum_numbers(number_1, number_2))