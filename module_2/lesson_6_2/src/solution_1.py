list_of_products = input("Введите товары через запятую: ").split(',')
print(f"Товары с нечетным индексом: {','.join(list_of_products[1::2])}")