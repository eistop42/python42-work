message = 'Hello world'
message = 'Hello world new'

print(message)

a = int(input('Введи число: '))
b = input('Введи число: ')
c = input('Введи число: ')


sum = int(a) - int(b) - int(c)
print('Результат', sum)
print(f'Результат {sum} - это вычитание')


km = input('Введи километры')
m = float(km) * 1000
print(f' {m} метров' )


a = int(input('введите длину'))
b = int(input('введите ширину'))

s = a * b
print(f'Площадь равна {s}')


age = int(input('веди возраст'))

if age >= 18 and 1 == 1:
    print('Вы совершеннолетний!')
else:
    print('доступ запрещен!')


login = input('введи логин')
password = input('введи пароль')

if login == 'admin' and password == '123':
    print('доступ разрешен')
else:
    print('доступ запрещен')


v = int(input('Введи скорость'))

if v > 150:
    print('Превышаешь!')
else:
    print('Нормальная скорость')