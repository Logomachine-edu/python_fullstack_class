first_shop = set(input('Первый магазин: ').split(', '))
second_shop = set(input('Второй магазин: ').split(', '))
print(f'Только в первом магазине: {", ".join(first_shop.difference(second_shop))}')
print(f"Только во втором магазине: {', '.join(second_shop.difference(first_shop))}")