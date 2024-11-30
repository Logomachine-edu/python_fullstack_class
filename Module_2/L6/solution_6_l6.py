products = input('Введите товары через запятую: ').split(', ')
pos_for_new = int(input('Позиция для нового товара: '))
new_product = input('Введите новый товар: ')
pos = pos_for_new - 1
products.insert(pos, new_product)
print('Товары на полке:', ', '.join(products))