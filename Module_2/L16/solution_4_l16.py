def create_shelves(sales):

    products = sales.split(';')
    products_sales = [list(map(int, product.split(","))) for product in products]

    return products_sales


shelves_1 = create_shelves("5,3;7,2")
shelves_2 = create_shelves("2,6,4;3,5,7;1,2,3")


print(f"Продажи: {shelves_1}")
print(f"Продажи: {shelves_2}")