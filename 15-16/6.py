users = {'tom': '1dfs23', 'sam': '12d3451', 'petr': 'dfe1232'}

login = input('Введи логин')
password = input('Введи пароль')

if login in users.keys():
    print('ты есть')
    if password == users[login]:
        print('ты вошел!')
    else:
        print('не правильный пароль')
else:
    print('тебя нет в базе')