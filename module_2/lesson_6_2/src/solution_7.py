list_of_products = input('Введите товары через запятую: ').split(',')
position_to_delete = int(input("Позиция для удаления товара: "))
list_of_products.pop(position_to_delete - 1)
print(f'Товары на полке: {",".join(list_of_products)}')