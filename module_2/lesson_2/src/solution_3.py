books_quantity: int = int(input("Количество книг: "))
stationery_quantity: int = int(input("Количество канцтоваров: "))
toys_quantity: int = int(input("Количество игрушек: "))

total_volume: float = round(((books_quantity * 2) + (stationery_quantity * 1.5) + (toys_quantity * 3)), 1)

print("Общий объем: " + str(total_volume) + " м^3")