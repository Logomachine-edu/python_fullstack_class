prices = input('Введите список цен:').split(",")
prices_numbers = [int(x) for x in prices]


def calculate_discount(data, i = 0):
    prices_discoint = []
    if len(data) == 0 :
        return None 
    elif len(data) == 1:
        return data
    else:
        prices_discoint = calculate_discount(data[1:])
        if  i == 0:
            prices_discoint.append(data[i])
            i += 1
            return prices_discoint
        else:
            prices_discoint.append(data[i] - prices_discoint[i-1] * 0.1)
            i += 1
            return prices_discoint

       


print("Итоговый список:" , calculate_discount(prices_numbers))
