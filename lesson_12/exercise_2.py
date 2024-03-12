def check_order(data: dict) -> bool:
    return len(data['items']) != 0


def package_order(data: dict):
    return f'Отправка: Упакован заказ {data['id']}'


def send_order(check_order_, package_order_, data):
    return package_order_(data) if check_order_(data) else f'Отправка: Заказ {data['id']} пуст'


order1 = {'id': 1, 'items': ['book', 'pen']}
order2 = {'id': 2, 'items': []}
print(send_order(check_order, package_order, order1))
print(send_order(check_order, package_order, order2))
