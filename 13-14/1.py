numbers_1 = [34,12,3,43,6]
numbers_2 = []

# перебрать все числа

for i in range(len(numbers_1)):
    if numbers_1[i] % 2 == 0:
        numbers_2.append(numbers_1[i])
print(numbers_2)
