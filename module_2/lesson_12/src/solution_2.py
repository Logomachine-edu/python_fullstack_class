from typing import Callable
order1 = {'id': 1, 'items': ['book', 'pen']}
order2 = {'id': 2, 'items': []}

def check_order(dct):
    if len(dct["items"]) > 0:
        return True
    else:
        return False


def package_order(dct):
    return f"Упакован заказ {dct['id']}"


def send_order(func: Callable[[int], int], func_2: Callable[[int], int], dct: dict):
    if func(dct) == True:
        return f"Отправка: {func_2(dct)}"
    else:
        return f"Отправка: Заказ {dct['id']} пуст"


print(send_order(check_order, package_order, order1))
print(send_order(check_order, package_order, order2))