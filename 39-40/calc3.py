
class Calc():

    def __init__(self, name):
        self.count = 0
        self.user_name = name

    def hello(self):
        print(f'Привет {self.user_name}!')

    def buy(self):
        print(f'Пока... {self.user_name}')

    def add(self, number1, number2):
        self.count += 1
        return number1 + number2

    def subtract(self, number1, number2):
        self.count += 1
        return number1 - number2

    def multiply(self, number1, number2):
        self.count += 1
        return number1 * number2

    def divide(self, number1, number2):
        self.count += 1
        return number1 / number2



user = input('Введи имя:')

# создание экземпляра класса
calculator1 = Calc(name=user)
# вызываем метод
calculator1.hello()

while True:
    number1 = int(input('Первое число:'))
    number2 = int(input('Второе число:'))
    action = input('Действие: +/-*')

    if action == '+':
        res = calculator1.add(number1, number2)
        print(res)
    elif action == '-':
        print(calculator1.subtract(number1, number2))
    elif action == '*':
        print(calculator1.multiply(number1, number2))
    elif action == '/':
        print(calculator1.divide(number1, number2))
    elif action == 'q':
        calculator1.buy()
        break
    else:
        print('не то действие')


print(f'Кол-во операций: {calculator1.count}')

