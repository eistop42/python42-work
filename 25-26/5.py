users = []

def add_user(name, users):
    if name not in users:
        users.append(name)
    return users

users = add_user('Антон', users)
users = add_user('Алиса', users)
users = add_user('Алиса', users)

print(users)