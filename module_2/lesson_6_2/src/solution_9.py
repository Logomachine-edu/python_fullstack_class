list_of_prices = map(int, input('Введите цены: ').split(','))
print(f'Отсортированные цены: {sorted(list_of_prices, reverse=True)}')