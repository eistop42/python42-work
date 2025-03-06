# Напишите функцию, которая рассчитывает стоимость яблок.
# Функция принимает вес, цену за 1кг и необязательный аргумент в виде скидки в процентах.
# Функция должна рассчитывать итоговую стоимость, учитывая скидку, если она есть.


def get_price(weight, price, discount=None):
    sum = weight * price

    if discount:
        sum = sum - (sum * discount/100)
    return sum


print(get_price(5, 100))
print(get_price(5, 100, 30))