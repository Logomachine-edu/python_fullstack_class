list_of_products = input('Введите товары через запятую: ').split(',')
product_location = int(input('Позиция для нового товара: '))
new_product = input('Введите новый товар: ')
list_of_products.insert(product_location - 1, new_product)
print(f'Товары на полке: {list_of_products}')

