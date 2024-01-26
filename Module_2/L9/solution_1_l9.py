def calculate_discount(price):
    prices = price[:-1]
    sum_prices = sum(prices)
    disc = sum_prices * (price[-1] / 100)
    return disc

print(f"Сумма скидки: {round(calculate_discount([100, 200, 300, 10]))}")
print(f"Сумма скидки: {round(calculate_discount([50, 150, 250, 20]))}")