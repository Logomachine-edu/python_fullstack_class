first_products = set(input("Введите список продуктов первого магазина через запятую:").split(","))
second_products = set(input("Введите список продуктов второго магазина через запятую:").split(","))
general_products = first_products & second_products
result = ( first_products | second_products ) - general_products
print(result)