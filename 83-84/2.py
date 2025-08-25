import re

names = 'alisa 123 bob 3940 anton'
user = 'question_id=33&answer_id=4'

r = re.findall(r'[a-z]+', names)
r1 = re.findall(r'\d+', names)
r2 = re.search(r'^question_id=\d+', user)
r3 = re.findall(r'question_id=(\d+)&answer_id=(\d+)', user)[0]
print(r3)