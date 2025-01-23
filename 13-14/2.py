numbers = [43, 5, -1, 4, 12]

min_number = numbers[0]

for i in range(len(numbers)):
    # надо сравнить элемент с min_number
    if numbers[i] < min_number:
        min_number = numbers[i]
print(min_number)