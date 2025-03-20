users = []

def add_phone(name, phone):
    user = {'name': name, 'phone': phone}
    users.append(user)
    print(users)


def get_phone(name):
    for user in users:
        if user['name'] == name:
            return user['phone']

    return 'нет такого имени'

while True:
     print("\nЧто вы хотите сделать?")
     print("1 - Добавить номер телефона")
     print("2 - Узнать номер телефона по имени")
     print("3 - Выйти")

     choice = input("Введите номер действия: ")

     if choice == "1":
        name = input('имя: ')
        phone = input('телефон: ')
        add_phone(name, phone)
     elif choice == "2":
        name = input('имя: ')
        print(get_phone(name))
     elif choice == "3":
        print("Выход из программы.")
        break
     else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")