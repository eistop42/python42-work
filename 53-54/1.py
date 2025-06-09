class Order:
    def __init__(self, items, shipping_type):
        self.items = items
        self.shipping_type = shipping_type

    def get_total_cost(self):
        price = 0
        for item in self.items:
            price += item['price']
        return price

    def get_total_weight(self):
        weight = 0
        for item in self.items:
            weight += item['weight']
        return weight

    def get_shipping_cost(self):
        total_weight = self.get_total_weight()
        total_cost = self.get_total_cost()

        if self.shipping_type == 'air':
            return total_weight * 500
        elif self.shipping_type == 'ground':
            if total_cost >= 100:
                return 0
            else:
                return total_weight * 200

items = [{'price': 50, 'weight': 2},
         {'price': 30, 'weight': 1.5},
         {'price': 20, 'weight': 1}]

order = Order(items, 'ground')

print(order.get_shipping_cost())
