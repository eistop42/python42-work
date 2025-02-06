words = {'кот': 'cat', 'собака': 'dog', 'идти': 'go', 'гулять': 'walk'}

user = 'кот идти гулять'

words_list = user.split()

s = ''

for word in words_list:
    if word in words:
        w = words[word]
        s = s + ' ' + w

print(s)


