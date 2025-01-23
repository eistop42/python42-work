
text = "Для того чтобы изучить программирование нужно всего лишь изучать его и все"

secret = ['программирование', 'изучать', 'его']

l = text.split(' ')
print(l)

for i in range(len(l)):
    if l[i] in secret:
        l[i] = '*'
print(l)
s = " ".join(l)
print(s)