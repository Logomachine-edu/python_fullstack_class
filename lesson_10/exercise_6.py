def find_max_price(price_list):
    if len(price_list) == 0:
        return 0
    elif len(price_list) == 1:
        return price_list[0]
    elif price_list[0] - price_list[1] > 0:
        price_list.pop(1)
        return find_max_price(price_list)
    else:
        price_list = price_list[1:]
        return find_max_price(price_list)


print(find_max_price([15, 7, 9]))
print(find_max_price([1, 10, 20, 5]))
print(find_max_price([25, 25, 25]))
print(find_max_price([10, 8, 12]))
