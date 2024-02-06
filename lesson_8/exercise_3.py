goods: dict[str, int] = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
max_price = max(goods.values())
min_price = min(goods.values())
goods_min = [key for key in goods if goods[key] == min_price]
goods_max = [key for key in goods if goods[key] == max_price]
print("Самый дешевый:", "".join(goods_min), "-", min_price, "руб.")
print("Самый дорогой:", "".join(goods_max), "-", max_price, "руб.")
