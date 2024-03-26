def create_shelves():
    num_shelves = int(input("Введите количество полок: "))
    shelf_lengths = list(map(int, input("Введите длины полок через запятую: ").split(',')))
    items = list(map(int, input("Введите кол-во товаров через запятую: ").split(',')))

    shelves_goods = [[length, goods] for length, goods in zip(shelf_lengths, items)]

    return shelves_goods

shelves_goods = create_shelves()
print(f"Полки: {shelves_goods}")