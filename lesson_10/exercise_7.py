def calculate_discount(lst):
    if len(lst) == 1:
        return [int(lst[0])]
    else:
        last_item = int(lst[-1]) - int(lst[-2] * 0.1)
        return calculate_discount(lst[:-1]) + [last_item]


print(calculate_discount([1000, 2000, 3000, 5000, 10000, 15000, 100, 200, 300, 400, 50, 100]))
