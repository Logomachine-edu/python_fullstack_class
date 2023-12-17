prices = input('Введите цены: ').split(', ')
price = list(map(int, prices))
sort_price = price[::-1]
print('Отсортированные цены:', ', '.join(map(str, sort_price)))