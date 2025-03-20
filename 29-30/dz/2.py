import json
#
# data = [
#     {'name': 'anton', 'password': 123},
#     {'name': 'alisa', 'password': 12345},
# ]
#
# with open('users.json', 'w') as f:
#     json.dump(data, f)

with open('users.json') as f:
    data = json.load(f)
    print(data)

def auth(name, password):
    with open('users.json') as f:
        data = json.load(f)
    for user in data:
        if user['name'] == name:
            if user['password'] == password:
                return True
            else:
                return False

name = input('введи имя: ')
passw = input('введи пароль: ')

is_auth = auth(name, passw)

if is_auth == True:
    print('добро пожаловать')
else:
    print('нет доступа')

