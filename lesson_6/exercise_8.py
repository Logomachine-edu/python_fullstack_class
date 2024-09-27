def swapping(products, index_1, index_2):
    index_1 -= 1
    index_2 -= 1
    products[index_1], products[index_2] = products[index_2], products[index_1]
    print("На полке:", ", ".join(products))


swapping(["Чай", "Мед", "Сахар"], 1, 3)
