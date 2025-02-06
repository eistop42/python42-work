users = [{'name': 'anton', 'password': '123', 'city': 'EKB'},
        {'name': 'vlad', 'password': 'werw', 'city': 'Moscow'},
        {'name': 'kolya', 'password': '324523', 'city': 'SPB'}
        ]

login = input('логин: ')
password = input('пароль: ')
find = 0

for user in users:
    if login == user['name'] and password == user['password']:
        print(f'Привет {login} из {user['city']}')
        find = 1
        break

print(find)
if find == 0:
    print('неверный логин или пароль')

