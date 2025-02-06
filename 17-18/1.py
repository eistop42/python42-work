while True:
    s = input('введи выражение')

    number_1 = int(s[0])
    number_2 = int(s[2])

    if s[1] == '+':
        print(number_1 + number_2)
    elif s[1] == '-':
        print(number_1 - number_2)
    elif s[1] == '*':
        print(number_1 * number_2)
    elif s[1] == '/':
        print(number_1 / number_2)