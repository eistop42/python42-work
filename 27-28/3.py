def read_file():
    with open('products.txt', 'r', encoding='utf-8') as f:
        n = 1
        lines = f.readlines()
        print(lines)
        for line in lines:
            print(f'{n}.{line}')
            n += 1
    return lines

def write_file(lines):
    with open('products.txt', 'w', encoding='utf-8') as f:
        f.writelines(lines)


products = read_file()
number = int(input('какой номер хочешь удалить?'))

products.pop(number-1)

write_file(products)

