
students = [
    {"name": "Антон", "математика": 85, "физика": 90},
    {"name": "Мария", "математика": 78, "химия": 95},
    {"name": "Лев", "литература": 78, "математика": 50}
]

subjects = ['математика', 'физика', 'химия', 'литература']


max_mark = 0

for name in students:
    mark = 0
    count = 0
    for subject in subjects:
        if subject in name:
            mark += name[subject]
            count += 1
    middle = mark/count
    if middle > max_mark:
        max_mark = middle
        max_name = name['name']

print(max_mark, max_name)

