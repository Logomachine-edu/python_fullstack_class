products = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
max_product = max(products, key = products.get)
min_product = min(products, key = products.get)
print(f"Самый дешевый: {min_product} - {products[min_product]} руб.")
print(f"Самый дорогой: {max_product} - {products[max_product]} руб.")