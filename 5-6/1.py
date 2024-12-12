
user = input('Выбери: к, н или б')
comp = input('Выбери: к, н или б')


if user == comp:
    print('ничья')

elif (user == 'к' and comp == 'н' ) or (user == 'б' and comp == 'к') or ( user == 'н' and comp == 'б'):
    print('выиграл')

else:
    print('ты проиграл')