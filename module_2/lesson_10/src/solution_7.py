prices = input('Введите список цен:').split(",")
prices_numbers = [int(x) for x in prices]


def calculate_discount(data, i = 1):
    prices_discoint = prices_numbers[:1:]
    if i < len(data):
        prices_discoint.append(prices_numbers[i]-(prices_numbers[i-1]*0.1))
        i += 1
        return prices_discoint
    calculate_discount(data)          
    return prices_discoint  

print("Максимальная цена:" , calculate_discount(prices_numbers))
