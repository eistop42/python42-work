import random

questions = ['Столица России?', 'Самая высокая гора?']
answers = ['Москва', 'Эверест']

q = random.choice(questions)
print(q)
user = input('ответ: ')

# Сравнить ответ пользователя с ответом из базы

ind = questions.index(q)
if user == answers[ind]:
    print('Верно!')
else:
    print('нет')