# Пользователь вводит с клавиатуры два числа.
# Необходимо найти сумму чисел, разницу чисел, произведение числе.
# Результат вычислений вывести на экран.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

sum = a + b
mult = a * b
div = a - b

print(f'Сумма: {sum}')
print(f'Произведение: {mult}')
print(f'Разность: {div}')


