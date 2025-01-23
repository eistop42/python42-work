import random

numbers = []

for i in range(10):
    num = random.randint(-50, 50)
    numbers.append(num)
print(numbers)

neg_numbers = 0
even_numbers = 0
uneven_numbers = 0
index_numbers = 1

for i in range(len(numbers)):
    if numbers[i] < 0:
        neg_numbers = neg_numbers + numbers[i]
    if numbers[i] % 2 == 0:
        even_numbers += numbers[i]
    if numbers[i] % 2 != 0:
        uneven_numbers += numbers[i]
    if i % 3 == 0:
        index_numbers *= numbers[i]


print(neg_numbers)
print(even_numbers)
print(uneven_numbers)
print(index_numbers)