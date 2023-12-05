prices = [1000,2000,3000,4000]
prices_numbers = [int(x) for x in prices]


def calculate_discount(data):
    if len(data) == 1:
        return [data[0]]
    else:
        last = int(data[-1] - data[-2] * 0.1)
        return calculate_discount(data[:-1]) + [last]
       


print("Итоговый список:" , calculate_discount(prices))
