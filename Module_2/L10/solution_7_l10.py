def calculate_discount(prices, index = 0, prev_price = None):
    changed_price = []
    if index < len(prices):
        new_price = prices[index]
        discount = int(prev_price * (10 / 100) if prev_price is not None else 0)
        discounted_price = new_price - discount if prev_price is not None else new_price
        changed_price.append(discounted_price)
        changed_price += calculate_discount(prices, index + 1, new_price)
    return changed_price

prices = [1000, 2000, 3000]
total_price = ', '.join(map(str, calculate_discount(prices)))

print(f"Цена со скидкой: {total_price}")