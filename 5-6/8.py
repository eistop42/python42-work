# Напишите программу, которая проверяет состоит ли
# строка только из цифр, только из букв или из букв и цифр вместе.
#
# *условные операторы, методы строк


word = input('Введи слово: ')

if word.isalpha() == True:
    print('Строка состоит из букв!')
elif word.isdigit() == True:
    print('Строка состоит из цифр!')
else:
    print('из букв и цифр')