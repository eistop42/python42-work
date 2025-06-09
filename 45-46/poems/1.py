
class Poems:
    def __init__(self):
        self.poems = []

    def add(self, author: str, name: str, year: int):

        for poem in self.poems:
            if poem['name'] == name and poem['author'] == author:
                print('Такое уже есть')
                break
        else:
            poem = {'name': name, 'author': author, 'year': year}
            self.poems.append(poem)

    def get_info(self):
        print(self.poems)

poems = Poems()
poems.add('Пушкин', 'Друзьям', 1816)
poems.add('Лермонтов', 'Весна', 1830)
poems.add('Пушкин', 'Друзьям', 1816)
poems.add('Пушкин', 'План', 1817)
poems.add('Рыжий', 'В России растаются навсегда...', 1996)
poems.get_info()