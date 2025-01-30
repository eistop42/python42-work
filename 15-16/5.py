users = {'tom': '1dfs23', 'sam': '12d3451', 'petr': 'dfe1232'}

for key in users:
    print(key)


for key, value in users.items():
    s = f'Логин: {key}, Пароль: {value}'
    print(s)