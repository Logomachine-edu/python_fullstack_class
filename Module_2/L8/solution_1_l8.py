products = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
product = input('Введите товар: ')

if product in products:
    print('Цена:', products[product], 'руб.')
else:
    print('Данного товара нет в списке.')