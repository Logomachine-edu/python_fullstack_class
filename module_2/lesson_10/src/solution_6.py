prices = input('Введите список цен:').split(",")
prices_numbers = [int(x) for x in prices]


def find_max_price(data, i = 0):
    max_price = 0
    if i < len(data) and max_price < data[i]:
        max_price = data[i]
        return max_price
    else:
        return find_max_price(data , i+1)        

print("Максимальная цена:" , find_max_price(prices_numbers))
