english = {'кот': 'cat', 'собака': 'dog'}

points = 0
for word in english:
    user = input(f'Введи перевод слова {word} ')

    if user == english[word]:
        print('верно')
        points += 1
    else:
        print('не так')

print(f'Набрано баллов {points}')
