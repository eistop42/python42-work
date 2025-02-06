users = [{'name': 'anton', 'password': '123', 'city': 'EKB'},
        {'name': 'vlad', 'password': 'werw', 'city': 'Moscow'},
        {'name': 'kolya', 'password': '324523', 'city': 'SPB'}
        ]

name = input('введи имя: ')
password = input('введи пароль: ')
city = input('введи город: ')

u_dict = {'name': name, 'password': password, 'city': city}
users.append(u_dict)

print(users)

