new_product = ["Мед"]
products: list[str] = ["Чай", "Кофе", "Сахар"]
products.insert(1, new_product[0])
print("Товары на полке:", ", ".join(products))
