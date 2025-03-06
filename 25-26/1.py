a = int(input('Первое число:'))
b = int(input('Второе число:'))


def event(number1, number2):
    sum = 0
    for i in range(number1, number2+1):
        if i % 2 == 0:
            sum += i
    return sum

print(event(a, b))
