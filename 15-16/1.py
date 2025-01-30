import random

adj = ['красивый', 'мудрый', 'волнующий', 'печальный']
noun1 = ['закат', 'ключ', 'эксперимент', 'код']
noun2 = ['единорога', 'ребенка', 'президента', 'вселенной']

# выбрать рандомные значения из каждого списка
# составить из этих значение предложение и вывести на экран


res_adj = random.choice(adj)
res_noun1 = random.choice(noun1)
res_noun2 = random.choice(noun2)

print(res_adj, res_noun1, res_noun2)
