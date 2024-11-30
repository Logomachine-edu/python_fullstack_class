list_of_products = input('Введите товары: ').split(',')
products_index_1, products_index_2 = map(int, input('Позиции для перестановки: ').split(','))
list_of_products[products_index_1 - 1], list_of_products[products_index_2 - 1] = list_of_products[products_index_2 - 1], list_of_products[products_index_1 - 1]
print(f'На полке: {list_of_products}')