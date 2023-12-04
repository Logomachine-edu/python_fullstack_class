prices = input('Введите список цен:').split(",")
prices_numbers = [int(x) for x in prices]


def find_max_price(data, i = 0):
    max_price = 0
    if len(data) == 0 :
        return None 
    elif len(data) == 1:
        max_price = data[0]
        return max_price
    else:
        max_price = find_max_price(data[1:]) 
        if data[0] > max_price:
            max_price = data[0]
            return max_price
        else:
            return max_price        

print("Максимальная цена:" , find_max_price(prices_numbers))
