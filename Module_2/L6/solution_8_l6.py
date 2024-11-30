products = input('Введите товары: ').split(', ')
rev_1, rev_2 = int(input('Позиции для перестановки: ')), int(input('Позиции для перестановки: '))
products[rev_1 - 1], products[rev_2 - 1] = products[rev_2 - 1], products[rev_1 - 1]
print('Товары на полке:', ', '.join(products))