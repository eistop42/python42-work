number = int(input('введи число: '))

count = 1
for i in range(1, number+1):
    count = count * i
    # print(i)
print(count)