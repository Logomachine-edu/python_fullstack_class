"""Программа для ведения системы учета запасов.
"""


def update_stock(item, quantity, stock):
    """Обновляем остатки запаса товаров.
    """
    if item in stock:
        stock[item]['quantity'] += quantity
    else:
        stock[item] = {'quantity': quantity}


def get_item_quantity(item_name, stock):
    """Получаем количество определенного товара.
    """
    return stock[item_name]['quantity']


def remove_item(item, stock):
    """Убираем сведения о ненужном товаре.
    """
    if item in stock:
        del stock[item]


reserve = {}

update_stock('Apple', 50, reserve)
update_stock('Banana', 30, reserve)
update_stock('Coffee', 20, reserve)

print(get_item_quantity('Apple', reserve))

remove_item('Banana', reserve)

print(reserve)
