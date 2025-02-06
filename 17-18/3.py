words = {'кот': 'cat', 'собака': 'dog'}

while True:
    word = input('введи слово: ')
    translate = input('введи перевод: ')

    words[word] = translate

    print(words)