users = []

def add_user(name, **params):
    user = {'name': name}
    user.update(params)
    users.append(user)

add_user(name='Алиса', age='25', last_name='Селезнева')
add_user(name='Антон')

print(users)