
# Напишите программу “Викторину”.
# Задайте пользователю три вопроса.
# По итогам выведите количество баллов, которые набрал пользователь.
#
# *используйте несколько if, введите нужные переменные

ans1 = input('столица России?')
ans2 = input('самая высокая гора?')

if ans1 == 'Москва' and ans2 == 'Эверест':
    print('Вы набрали 2 балла')
elif ans1 == 'Москва' and ans2 != 'Эверест':
    print('Вы набрали 1 балл ')
elif ans1 != 'Москва' and ans2 == 'Эверест':
    print('Вы набрали 1 балл ')
else:
    print('Вы набрали 0 баллов')