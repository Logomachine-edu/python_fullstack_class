def calculate_discount(price):
    price_lst = price[:-1]
    sum_price = sum(price_lst)
    discount = sum_price * (price[-1] / 100)
    return discount


print(f'Сумма скидки: {calculate_discount([100, 200, 300, 10])}')
print(f'Сумма скидки:  {calculate_discount([50, 150, 250, 20])}')
