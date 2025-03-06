
def get_price(price, weight, discount=None):
    sum = price * weight

    if discount:
        sum = sum * 0.9
    return sum

price = int(input('введи цену'))
weight = int(input('введи вес'))
card = input('есть карта: да/нет')

if card == 'да':
    print(get_price(price, weight, True))
elif card == 'нет':
    print(get_price(price, weight))



