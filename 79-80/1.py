import sqlite3

con = sqlite3.connect('costs.db')
cur = con.cursor()
cur.execute('insert into costs (item, price) values (?, ?)', ('Хлеб', '50'))
con.commit()

with sqlite3.connect('costs.db') as conn:
    cur = conn.cursor()
    cur.execute('insert into costs (item, price) values (?, ?)', ('Молоко', '30'))

