import json

# products = [{'яблоко': 100, 'картошка': 200, 'ананасы': 500}]
# 
# with open('products.json', 'w', encoding='utf-8') as f:
#     json.dump(products, f)

with open('products.json', encoding='utf-8') as f:
    print(json.load(f))