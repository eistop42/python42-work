numbers = [[1,2, -3], [45, 3, -1]]
res = []
for number in numbers:
    count = 0
    for number1 in number:
        if number1 > 0:
            count += number1
    res.append(count)
print(res)