countries_data = [{'name': 'Россия', 'capital': 'Москва', 'people': 12000000},
             {'name': 'Китай', 'capital': 'Пекин', 'people': 23000000}]

# вывести словарь с Россией

for country in countries_data:
    if country['name'] == 'Россия':
        print(country)