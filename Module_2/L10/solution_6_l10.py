def find_max_price(prices):
    if len(prices) == 0:
        return None
    elif len(prices) == 2:
        if prices[0] > prices[1]:
            return prices[0]
        else:
            return prices[1]
    max_value = find_max_price(prices[1:])

    if prices[0] > max_value:
        return prices[0]
    else:
        return max_value
    
print(find_max_price([15, 7, 9]))
print(find_max_price([1, 10, 20, 5]))
print(find_max_price([25, 25, 25]))
print(find_max_price([10, 8, 12]))