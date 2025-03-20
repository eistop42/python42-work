import json

with open('products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for i in range(2):
    name = input('название продукта: ')
    price = input('цена продукта: ')

    products.append({name: price})

    print(products)

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f)

