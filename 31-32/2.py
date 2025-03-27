
# Напишите программу для создания списка дел. Программа должна спрашивать у пользователя действие:



import json


try:
    with open('tasks.json', encoding='utf-8') as f:
        tasks = json.load(f)

except FileNotFoundError:
    tasks = []
    print('Файла нет, создаю пустой список')


def add_task(task_name):
    # создает словарь для задачи, добавляет в глобальный список tasks
    task = {'name': task_name, 'status': 'не выполнена'}
    tasks.append(task)


def show_tasks():
    # показывает задачи
    for number, task in enumerate(tasks, start=1):
        print(f'{number}= {task['name']} - {task['status']}')

def save_tasks():
    # сохраняет текущие задачи в файл
    with open('tasks.json', 'w',  encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False)

def complete_task(number):
    # выполняет задачу
    tasks[number]['status'] = 'выполнена'


while True:
    print('Выбери: 1-добавить задачу, 2-посмотреть задачи, 3-выполнить задачу, 4 - выход')
    ans = input('ввведи число: ')
    if ans == '1':
        name = input('название задачи: ')
        add_task(name)
        save_tasks()
        print(tasks)
    if ans == '2':
        show_tasks()
    if ans == '3':
        show_tasks()
        num = int(input('Какую задачу выполнить: '))
        complete_task(num-1)
        save_tasks()
