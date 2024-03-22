list_products: dict[str: int] = dict(Яблоко = 100, Банан = 80, Кофе =  250, Чай = 150)

max_price = max(list_products, key = list_products.get)
min_price = min(list_products, key = list_products.get)

print(f'Самый дешёвый: {min_price} - {list_products[min_price]} руб.')
print(f'Самый дорогой: {max_price} - {list_products[max_price]} руб.')