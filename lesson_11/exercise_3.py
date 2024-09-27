def track_low_stock_with_for(product_dict, low_stock):
    print('Низкий запас: ')
    for product in product_dict:
        if product_dict.get(product) < low_stock:
            print(product, "-", product_dict[product])


track_low_stock_with_for({'apples': 50, 'bananas': 10, 'cherries': 3}, 15)
