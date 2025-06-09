class Animal():
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.health = 100

    def walk(self):
        self.health += 10
        print('Спасибо за прогулку', self.health)


class Dog(Animal):

    def speak(self):
        print('гав-гав')

    def eat(self, food):
        if food in ['мясо', 'кость']:
            self.health += 10
            print(f'Поел(а) {food}', self.health)
        else:
            self.health -= 10
            print('такое не ем', self.health)

class Cat(Animal):
    def speak(self):
        print('мяу-мяу')



dog = Dog(4, 'Тузик')
dog.walk()
dog.eat('мясо')
dog.eat('печенька')

cat = Cat(4, 'Барсик')
cat.speak()