list_products = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}

name_product = input('Введите товар: ')

if name_product in list_products:
    print(f'Цена: {list_products[name_product]} руб.')

else:
    print('Данного товара нет в наличии')