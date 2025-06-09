from abc import ABC, abstractmethod


class AbstractShipping(ABC):

    @abstractmethod
    def get_cost(self, order):
        pass


class AirShipping(AbstractShipping):

    def get_cost(self, order):
        total_weight = order.get_total_weight()
        return 500 * total_weight

class GroundSgipping(AbstractShipping):

    def get_cost(self, order):
        total_weight = order.get_total_weight()
        total_cost = order.get_total_cost()
        if total_cost >= 100:
            return 0
        return 200 * total_weight


class Order:
    def __init__(self, items, shipping_type: AbstractShipping):
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
        return self.shipping_type.get_cost(self)




items = [{'price': 50, 'weight': 2},
         {'price': 30, 'weight': 1.5},
         {'price': 20, 'weight': 1}]

air = AirShipping()
# ground = GroundShipping()
order = Order(items, air)
print(order.get_shipping_cost())
