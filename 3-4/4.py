# Напишите программу для перевода рублей в одну из валют.
# Пользователь должен ввести сначала количество рублей,
# потом название валюты.

rubles = int(input('Введите рубли: '))

currency = input('Введи название валюты: ')

if currency == 'доллар':
    res = rubles / 101
    print(f'Доллары: {res}')

elif currency == 'юань':
    res = rubles / 14
    print(f'Юани: {res}')

elif currency == 'евро':
    res = rubles / 120
    print(f'евро: {res}')
elif currency == 'евро':
    res = rubles / 120
    print(f'евро: {res}')
else:
    print('Такой валюты нет')
