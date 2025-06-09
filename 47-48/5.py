import random

words1 = ['красивый', 'мудрый']
words2 = ['закат', 'рассвет']
words3 = ['вселенной', 'мира']

for i in range(3):
    w1 = random.choice(words1)
    w2 = random.choice(words2)
    w3 = random.choice(words3)
    print(w1, w2, w3)