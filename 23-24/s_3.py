
n = 5

def factorial(number: int):
    s = 1
    for i in range(1, number+1):
        s = s * i
    return s

print(factorial(int(input('введи число'))))

