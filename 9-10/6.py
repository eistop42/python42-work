import time

n = int(input('введи секунды'))

while n > 0:
    n -= 1
    print(n)
    print('жди секунду')
    time.sleep(1)
print('время истекло')
