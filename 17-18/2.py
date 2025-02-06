names = ['антон', 'иван', 'егор', 'коля',]

balance = {'антон': 100, 'иван': 200, 'рома': 500, 'коля': 1000}


for name in names:

    # если имя есть в базе - вернуть занчение
    if name in balance:
        print(f'{name} : {balance[name]}')
