first_shop = set((input('Введите товары из первого магазина через запятую: ').split(", ")))
second_shop = set((input('Введите товары из второго магазина через запятую: ').split(", ")))
first_diff, second_diff = first_shop - second_shop, second_shop - first_shop
print(f"Только в первом магазине: {first_diff}")
print(f"Только во втором магазине: {second_diff}")