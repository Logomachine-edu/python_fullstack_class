first_shop_input = input('Введите товары из первого магазина через запятую: ')
first_shop = set(first_shop_input.split(', '))

second_shop_input = input('Введите товары из второго магазина через запятую: ')
second_shop = set(second_shop_input.split(', '))

only_in_first = first_shop.difference(second_shop)
only_in_second = second_shop.difference(first_shop)

print(f"Только в первом магазине {only_in_first}")
print(f"Только во втором магазине {only_in_second}")