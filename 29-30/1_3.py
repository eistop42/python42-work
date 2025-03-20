import json

with open('products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

def add_product(name, price):
    product = {name: price}
    products.append(product)
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f)

while True:
    ans = input('1-добавить товар, 2- посмотреть товары')

    if ans == '1':
        name = input('название продукта: ')
        price = input('цена продукта: ')
        add_product(name, price)

    if ans == '2':
        print(products)


