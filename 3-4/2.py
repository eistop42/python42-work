amount = int(input('Сумма покупок: '))

if amount > 1000:
    a = amount*0.9
    print(f'С учетом скидки: {amount}')
else:
    print(f'Cумма {amount}')