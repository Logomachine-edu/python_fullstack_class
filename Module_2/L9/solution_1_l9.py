price = list(map(int, input('Введите цены и скидку: ').split(", ")))

def calculate_discount(price):
    prices = price[:-1]
    sum_prices = sum(prices)
    disc = sum_prices * (price[-1] / 100)
    return disc

total = calculate_discount(price)
print(f"Сумма скидки: {total}")