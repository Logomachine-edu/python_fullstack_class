price: list[int] = [10, 20, 30, 40, 50]
price.sort()
print("Отсортированные цены:", end=" ")
print(*price[::-1], sep=", ")
