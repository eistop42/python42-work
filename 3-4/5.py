# Напишите программу, которая запрашивает у пользователя температуру (в градусах Цельсия) и выводит:
# "На улице холодно", если температура меньше 0.
# "На улице комфортно", если температура от 0 до 25 включительно.
# "На улице жарко", если температура больше 25.

temp = int(input('Введи температуру: '))

# первая версия
if temp > 25:
    print('На улице жарко')
elif temp > 0 and temp < 25:
    print('На улице комфортно')
elif temp < 0:
    print('на улице холодно')

# вторая версия
if temp > 25:
    print('На улице жарко')
elif temp > 0:
    print('На улице комфортно')
elif temp < 0:
    print('на улице холодно')