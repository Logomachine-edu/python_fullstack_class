list_price_and_discount = list(map(int, input('Введите цены и скидку: ').split(',')))
def calculate_discount(list_prise_and_discount):
    discount = list_price_and_discount[-1]
    list_prices = sum(list_price_and_discount[:-1])
    discount_amount = (discount * list_prices) // 100
    return discount_amount
print(f"Сумма скидки: {calculate_discount(list_price_and_discount)}")