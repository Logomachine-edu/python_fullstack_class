products = input('Введите товары через запятую: ').split(', ')
pos_for_del = int(input('Позиция для удаления товара: '))
pos = pos_for_del - 1
products.pop(pos)
print('Товары на полке:', ', '.join(products))