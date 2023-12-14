products: list[str] = ["Чай", "Мед", "Сахар"]
products[0], products[2] = products[2], products[0]
print("На полке:", ", ".join(products))
