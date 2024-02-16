def check_order(order):
    return bool(order.get('items'))

    
def package_order(order):
    return f"Упакован заказ {order['id']}"    
    
def send_order(check_order, package_order, order):
    if check_order(order):
        return f"Отправка: {package_order(order)}"
    else:
        return f"Отправка: Заказ {order['id']} пуст"

order_1 = {'id': 1, 'items': ['book', 'pen']}
order_2 = {'id': 2, 'items': []}


print(send_order(check_order, package_order, order_1))
print(send_order(check_order, package_order, order_2))