# login = 'admin'
# password = 123
#
# if login == 'admin' or password == 12345:
#     print('Доступ разрешен')
# else:
#     print("Доступ запрещен")
#


age = int(input('Введите возраст'))

days = int(age) * 365

if days >= 10000:
    print('Ух ты')
else:
    print(f'Ты прожил {days}')
