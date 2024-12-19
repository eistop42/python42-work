
count = 0
for i in range(4):
    user = input('столица России?').lower()
    if user == 'москва':
        print('Ответ верный 😎😎😎')
        count += 1
        break
    else:
        print('Ответ неверный 😐')
        count += 1
print(f'Потратил попыток: {count}')