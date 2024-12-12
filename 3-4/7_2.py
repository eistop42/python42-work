ans1 = input('столица России?')
ans2 = input('самая высокая гора?')

count = 0

if ans1 == 'Москва':
    count += 1
if ans2 == 'Эверест':
    count = count + 1

print(f'Набрано баллов {count}')
