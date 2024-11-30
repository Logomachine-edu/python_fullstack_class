prices = input('Введите цены: ').split(', ')
price = list(map(int, prices))
average = sum(price) // len(price)
print('Средняя цена товаров:', average)