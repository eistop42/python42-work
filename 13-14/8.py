countries = ['Италия', 'Индия', 'Россия', 'США', 'Китай', 'Нидерланды']
people = [58966453, 1434998000, 146150789, 341169410, 1409670000, 17967505]


min_people = people[0]
max_people = people[0]

for i in range(len(people)):
    if people[i] < min_people:
        min_people = people[i]
    if people[i] > max_people:
        max_people = people[i]

min_index = people.index(min_people)
max_index = people.index(max_people)

print(f'{countries[min_index]} : {min_people}')
print(f'{countries[max_index]} : {max_people}')