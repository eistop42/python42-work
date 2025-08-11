import sqlite3

# создание подключения
conn = sqlite3.connect('costs.db')

# создание курсора для выполнения запросов
cur = conn.cursor()

# создание таблицы

cur.execute("""CREATE TABLE IF NOT EXISTS
            costs (
                item text, 
                price integer check (price > 0), 
                id integer primary key autoincrement
                )
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS
            expensive_costs (
                item text, 
                price integer check (price > 0), 
                id integer primary key autoincrement
                )
            """)
#
# cur = conn.cursor()
# res1 = cur.execute(f'delete  from costs where id = 7 ')
# res2 = conn.commit()

def add_item(item, price):
    """Добавление траты в таблицу"""
    cur = conn.cursor()
    cur.execute(f'insert into costs (item, price) values (\'{item}\', {price})')
    conn.commit()

def add_expensive_item(item, price):
    """Добавление большой траты в  другую таблицу"""
    cur = conn.cursor()
    cur.execute(f'insert into expensive_costs (item, price) values (\'{item}\', {price})')
    conn.commit()

def get_item_by_id(item_id):
    """Получить товар по id"""
    cur = conn.cursor()
    cur.execute(f'select * from costs where id = {item_id}')
    item = cur.fetchone()
    return item

def get_items():
    """Получить данные из таблицы трат"""
    cur = conn.cursor()
    cur.execute('select * from costs')
    items = cur.fetchall()
    for item in items:
        print(f'Название: {item[0]}, Цена: {item[1]}, ID: {item[2]}')

def del_item(item_id):
    """удаление товара из трат"""
    cur = conn.cursor()
    cur.execute(f'delete  from costs where id = {item_id}')
    conn.commit()

while True:
    print('1 - добавить товар, 2 - посмотреть траты, 3 - удалить товар,  0 - выход')
    action = input('Выбери действие: ')
    if action == '1':
        item = input('Введи название товара: ')
        price = int(input('Введи цену товара: '))

        if price < 1000:
            add_item(item, price)
        else:
            add_expensive_item(item, price)

    elif action == '2':
        # сходить в базу и вывести содержимое таблицы
        items = get_items()
    elif action == '3':
        get_items()
        item_id = input('Введи id товара')

        # проверить, что такой id есть
        item = get_item_by_id(item_id)
        if item != None:
            del_item(item_id)
            print('==Товар удален!==')
            get_items()
        else:
            print('такого товара нет')
    elif action == '0':
        break
# delete from costs where id = 1;
conn.close()

