
class Calc:

    def __init__(self, logger):
        self.logger = logger

    def add(self, number1, number2):
        res = number1 + number2
        self.logger.log(number1, number2, res, 'Сумма')

        return res


class Logger:
    def log(self, number1, number2, res, operation):
        with open('logs.txt', 'a', encoding='utf-8') as f:
            f.write(f'{operation} - {number1, number2} Результат {res} \n')

logger = Logger()
calc = Calc(logger)
print(calc.add(9,12))

# s = 'sdf'
# s.count()