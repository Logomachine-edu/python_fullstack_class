def track_low_stock_with_for(goods, count):
    print('Низкий запас: ')
    
    for product, values in goods.items():
        if values < count:
            print(f'{product} - {values}')

track_low_stock_with_for({'apples': 50, 'bananas': 10, 'cherries': 3}, 15)