price_1: list[str] = ['50', '45', '30', '25']
price_2: list[str] = ['100', '90', '85', '70', '60']
print("Цены без скидки:", ", ".join(map(str, price_1[1::2])))
print("Цены без скидки:", ", ".join(map(str, price_2[1::2])))
