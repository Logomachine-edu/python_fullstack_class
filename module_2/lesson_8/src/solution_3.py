products: dict[str , int] = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
max_prod = max(products, key=products.get)
min_prod = min(products, key=products.get)

print("Самый дорогой товар -" , max_prod , "-" , products[max_prod] , "\n" , "Самый дешевый товар -" , min_prod , "-" , products[min_prod] )


