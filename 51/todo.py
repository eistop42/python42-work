import json
from abc import abstractmethod, ABC

from rich.console import Console
from rich.table import Table

class Model:

    def add_task(self, task_name):
        #записать задачу в json файл
        tasks = self._load_from_file()
        tasks.append(task_name)
        self.save_tasks(tasks)

    def save_tasks(self, tasks):
        with open('tasks.json', 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False)

    def get_tasks(self):
        return self._load_from_file()

    def del_task(self, number):
        tasks = self.get_tasks()
        if 0 <= number <= len(tasks)-1:
            tasks.pop(number)
            print('удалил задачу')
        else:
            print('неверный номер')
        self.save_tasks(tasks)


    def _load_from_file(self):
        with open('tasks.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)
            return tasks


class AbstractView(ABC):

    @abstractmethod
    def show_tasks(self):
        pass
    

class View(AbstractView):

    def show_tasks(self, tasks):
        for number, task in enumerate(tasks, start=1):
            print(number, task)


class RichView(AbstractView):

    def show_tasks(self, tasks):
        console = Console()
        table = Table(title="TODO List")

        table.add_column("Number", justify="center", style="blue")
        table.add_column("Name", justify="center", style="yellow")


        for number, task in enumerate(tasks, start=1):
            table.add_row(str(number), task)
        console.print(table)


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def add_task(self, task_name):
        print(task_name)
        # вызвать метод сохранения данных в базу
        self.model.add_task(task_name)

    def show_tasks(self, view_type):
        # вывести все задачи
        tasks = self.model.get_tasks()
        if view_type == 'rich':
            v = RichView()
            v.show_tasks(tasks)
        else:
            v = View()
            v.show_tasks(tasks)

    def del_task(self, number):
        self.show_tasks()
        number = int(input('Выбери номер для удаления'))
        self.model.del_task(number-1)
        self.show_tasks()



model = Model()
view = View()
rich_view = RichView()


cont = Controller(model, rich_view)



while True:
    print('1.Добавить задачу\n2.Показать задачи\n3.Удалить задачу')
    answer = input('Выбери действие: ')
    if answer == '1':
        task = input('Введи название задачи:')
        cont.add_task(task)
    elif answer == '2':
        cont.show_tasks()
    elif answer == '3':
        cont.del_task()