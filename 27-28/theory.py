
# запись в файл
f = open('test.txt', 'w')
f.write('hello')
f.close()

# добавление
f = open('test.txt', 'a')
f.write('hello')
f.close()

# чтение всего содержимого
f = open('test.txt', 'r')
print(f.read())
f.close()

# чтение всего содержимого c записью в список
f = open('test.txt', 'r')
print(f.readlines())
f.close()

# чтение строчка за строчкой
f = open('test.txt', 'r')
for line in f:
    print(line)
f.close()


#открытие файла контекстными менеджерами
with open('test.txt', 'r') as f:
    print(f.read())


# w - write
# r - read
# a - append