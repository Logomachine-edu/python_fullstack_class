products: list[str] = ["Чай", "Кофе", "Сахар", "Мед"]
products.pop(1)
print("Товары на полке:", ", ".join(products))
