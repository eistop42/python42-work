import random

brain = {'привет': ['добрый вечер!', 'здарова'], 'как дела': ['хорошо', 'неоч'], 'температура': [15, -30]}


while True:
    user = input('ввод: ')

    if user in brain.keys():
        print(random.choice(brain[user]))
