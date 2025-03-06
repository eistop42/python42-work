users = []

def add_user(name, age=18):

    print(f'Имя {name} Возраст {age}')
    user = {'name': name, 'age': age}
    users.append(user)

add_user(age=24, name='Антон')
add_user(age=20, name='Алиса')
add_user(age=18, name='Марк')

print(users)