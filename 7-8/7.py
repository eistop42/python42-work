number1 = int(input('Введи число'))
number2 = int(input('Введи число'))

count = 0
count2 = 0

for i in range(number1, number2+1, 1):
    count = count + i
    count2 = count2 + 1

print(f"Cумма: {count}")
print(f"Среднее арифмитическое:  {count/count2}")