import sqlite3

class DB:
    def __init__(self, db_name):
        self.db_name = db_name

    def get_costs(self):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            data = cur.execute('SELECT * FROM costs').fetchall()
        return data

    def add_cost(self, name, price):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            cur.execute('insert into costs (item, price) values (?, ?)', (name, price,  ))

    def add_user(self, telegram_id, first_name):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            cur.execute('insert into users (telegram_id, first_name) values (?, ?)', (telegram_id, first_name,  ))

    def get_user_by_id(self, telegram_id):
        """Получить пользователя по телеграм id"""
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            data = cur.execute(f'SELECT * FROM users where telegram_id = {telegram_id}').fetchone()
        return data

db = DB('costs.db')

# print(db.get_user_by_id(158448812))
# print(db.get_user_by_id(234234))