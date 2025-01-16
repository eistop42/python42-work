# 1. найти все четные числа
# 2. найти самое большое число

s = [12, 3, 62,  21, ]

max_number = s[0]

for i in range(len(s)):
    if s[i] > max_number:
        max_number = s[i]
print(max_number)
