# 1. Вызов с числами

def sum_numbers(*args):
    s = 0
    for number in args:
        number = str(number)
        if number.isdigit():
            s += int(number)
    return s

def sum_numbers2(*args):
    s = 0
    for number in args:
        if isinstance(number, str):
            if number.isdigit():
                s += int(number)
        else:
            s += number
    return s

# result = sum_numbers('1', '2', '3', '4', '5')
result = sum_numbers2('10', '20', 'hello', '30', 'world', 40)
print(result)