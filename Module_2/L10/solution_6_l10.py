def find_max_price(prices):
    if len(prices) == 0:
        return None
    elif len(prices) == 1:
        return prices[0]
    else:
        max_price = find_max_price(prices[1:])
        return prices[0] if prices[0] > max_price else max_price

print(find_max_price([15, 7, 9]))
print(find_max_price([1, 10, 20, 5]))
print(find_max_price([25, 25, 25]))
print(find_max_price([10, 8, 12]))