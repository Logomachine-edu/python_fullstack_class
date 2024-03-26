def create_shelves():
    shelf_lengths = list(map(int, input("Введите длины полок через запятую: ").split(',')))

    shelves = [[length, 0] for length in shelf_lengths]

    return shelves

shelves = create_shelves()
print(f"Полки: {shelves}")