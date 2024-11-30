def generate_discount(shelves):

    discounts = []

    for i, shelf in enumerate(shelves):
        shelf_discount = []
        for j in range(1, shelf[1] + 1):
            discount = i + 1
            shelf_discount.append(discount * shelf[1])

        discounts.append(shelf_discount)

    return discounts


shelves_1 = generate_discount([[4, 2], [5, 3], [6, 5]])
shelves_2 = generate_discount([[3, 1], [4, 4]])

print(f"Скидки: {shelves_1}")
print(f"Скидки: {shelves_2}")