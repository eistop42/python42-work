# C использованием глобальной переменной users
users = []

def add_user(name):
    if name not in users:
        users.append(name)

add_user('Антон')
add_user('Алиса')
add_user('Алиса')

print(users)