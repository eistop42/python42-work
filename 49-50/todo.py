import json
from rich.console import Console
from rich.table import Table

class Model:

    def add_task(self, task_name):
        #записать задачу в json файл
        tasks = self._load_from_file()
        with open('tasks.json', 'w', encoding='utf-8') as f:
            tasks.append(task_name)
            json.dump(tasks, f, ensure_ascii=False)

    def get_tasks(self):
        return self._load_from_file()

    def _load_from_file(self):
        with open('tasks.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)
            return tasks


class View:

    def show_tasks(self, tasks):
        for number, task in enumerate(tasks, start=1):
            print(number, task)

class RichView:

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

    def show_tasks(self):
        # вывести все задачи
        tasks = self.model.get_tasks()
        self.view.show_tasks(tasks)



model = Model()
view = View()
rich_view = RichView()


cont = Controller(model, rich_view)



while True:
    print('1.Добавить задачу\n2.Показать задачи')
    answer = input('Выбери действие: ')
    if answer == '1':
        task = input('Введи название задачи:')
        cont.add_task(task)

    elif answer == '2':
        cont.show_tasks()