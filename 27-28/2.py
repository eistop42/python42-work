products = ['телефон', 'машина', 'планшет', 'компьютерная мышь']

with open('products.txt', 'w', encoding='utf-8') as f:
    for product in products:
        f.write(product)
        f.write('\n')
