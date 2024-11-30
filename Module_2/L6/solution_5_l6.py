price = input('Введите цены: ').split(', ')
prices = list(map(int, price))
min_price = prices.index(min(prices))
max_price = prices.index(max(prices))
price[min_price], price[max_price] = price[max_price], price[min_price]
print('Новые цены:', ', '.join(price))