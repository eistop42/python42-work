import json

with open('questions.json', encoding='utf-8') as f:
    data = json.load(f)

questions = data['questions']
score = 0

for question in questions:
    print(question['question'])
    for option in question['options']:
        print(option)
    ans = input('Введи ответ: ')
    
    if ans == question['correct_answer']:
        print('Верно!')
        score += 1
    else:
        print('Не верно')

print(f'Набрал баллов: {score}')