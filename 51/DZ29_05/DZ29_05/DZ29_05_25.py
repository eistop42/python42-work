import json

from rich.console import Console
from rich.table import Table

class Work:
    def add_prod_work(self, product):
        products = self._load_from_file()
        with open('products.json', 'w', encoding='utf-8') as f:
            products.append(product)
            json.dump(products, f)

    def get_show(self):
        return self._load_from_file()

    def _load_from_file(self):
        with open('products.json', 'r', encoding='utf-8') as f:
            products = json.load(f)
            return products

class Show:
    def show_work(self, products):
        for number, products in enumerate(products, start=1):
            print(number, products)

class ShowRich:
    def show_work(self, products):
        console = Console()
        table = Table(title='Просмотр покупок')
        table.add_column('Number', justify='center', style='red')
        table.add_column('Покупки', justify='center', style='green')
        table.add_column('Цена', justify='center', style='green')
        for number, product in enumerate(products, start=1):
            table.add_row(str(number), product['name'], str(product['price']))
        console.print(table)

    def five_price(self,products):
        products.sort(key=lambda product: product['price'], reverse = True)
        n = 1
        for product in products:
            if n <=5:
                print(f'{n} {product}')
                n +=1


class Controller:
    def __init__(self, work, show):
        self.work = work
        self.show = show

    def add_prod(self, name, prise):
        self.name = name
        self.prise = prise
        product = {'name': self.name, 'price': self.prise}
        print(f'{product} добавлены')
        self.work.add_prod_work(product)
    def show_prod(self):
        products = self.work.get_show()
        # print(products)
        self.show.show_work(products)
    def hi_prise(self):
        products = self.work.get_show()
        self.show.five_price(products)

work = Work()
show = Show()
product_name = Controller(work, show)
while True:
    print('1-добавление покупки\n2-просмотр покупки\n3-просмотр пяти самых дорогих покупок\n4-выход')
    product = input('введите номер пункта:')
    if product == '1':
        name = input('Введите наименование товара:')
        prise = int(input('Цена товара'))
        product_name.add_prod(name, prise)
    if product == '2':
        product_name.show_prod()
    if product == '3':
        product_name.hi_prise()
    if product == '4':
        exit()


# class Work:
#     def add_prod_work(self, product):
#         products = self._load_from_file()
#         with open('products.json', 'w', encoding='utf-8') as f:
#             products.append(product)
#             json.dump(products, f)
#
#     def get_show(self):
#         return self._load_from_file()
#
#     def _load_from_file(self):
#         with open('products.json', 'r', encoding='utf-8') as f:
#             products = json.load(f)
#             return products
#
# class Show:
#         def show_work(self, products):
#             for number, products in enumerate(products, start=1):
#                 print(number, products)
#
# # class Show:
# #     def show_work(self, products):
# #         a = list(products.item())
# #         print(a)
#         # console = Console()
#         # table = Table(title='Просмотр покупок')
#         # table.add_column('Number', justify='center', style='red')
#         # table.add_column('Покупки', justify='center', style='green')
#         # table.add_column('Покупки', justify='center', style='green')
#         # for number, product in enumerate(products['name'], products['price'], start=1):
#         #     table.add_row(str(number), product)
#         # console.print(table)
#
#
#
#     def five_price(self,products):
#         products.sort(key=lambda product: product['price'], reverse = True)
#         n = 1
#         for product in products:
#             if n <=5:
#                 print(f'{n} {product}')
#                 n +=1
#
#
# class Controller:
#     def __init__(self, work, show):
#         self.work = work
#         self.show = show
#
#     def add_prod(self, name, prise):
#         self.name = name
#         self.prise = prise
#         product = {'name': self.name, 'price': self.prise}
#         print(f'{product} добавлены')
#         self.work.add_prod_work(product)
#     def show_prod(self):
#         products = self.work.get_show()
#         # print(products)
#         self.show.show_work(products)
#     def hi_prise(self):
#         products = self.work.get_show()
#         self.show.five_price(products)
#
# work = Work()
# show = Show()
# product_name = Controller(work, show)
# while True:
#     print('1-добавление покупки\n2-просмотр покупки\n3-просмотр пяти самых дорогих покупок\n4-выход')
#     product = input('введите номер пункта:')
#     if product == '1':
#         name = input('Введите наименование товара:')
#         prise = int(input('Цена товара'))
#         product_name.add_prod(name, prise)
#     if product == '2':
#         product_name.show_prod()
#     if product == '3':
#         product_name.hi_prise()
#     if product == '4':
#         exit()


