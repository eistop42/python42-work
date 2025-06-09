class Counter():
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        print(f'Клики {self.count}')

        if self.count > 10:
            self._update_count()

    def decrement(self):
        self.count -= 1
        print(f'Клики {self.count}')

    def _update_count(self):
        print('Обнуляем клики')
        self.count = 0

c = Counter()
c.increment()
c.increment()
c.increment()
c.increment()
c.increment()
c.increment()
c.increment()
c.increment()
c.increment()
c.increment()
c.increment()
