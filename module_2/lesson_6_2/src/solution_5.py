prices = list(map(int, input('Введите цены: ').split(',')))
prices.sort
prices[0], prices[-1] = prices[-1], prices[0]
print(f'Новые цены: {prices}')