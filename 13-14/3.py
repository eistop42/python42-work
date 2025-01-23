numbers = [12, 4, 5, -3, 12, -6, 1, 7, 2]

# Сумму отрицательных чисел
# Сумму четных чисел
# Сумму нечетных чисел
# Произведение элементов с индексами кратными 3

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