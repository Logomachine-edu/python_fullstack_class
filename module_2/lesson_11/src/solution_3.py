products = {'apples': 50, 'bananas': 10 , 'cherries': 3}

def track_low_stock_with_for(arr):
    number = int(input("Введите порог:"))
    print(f'Низкий запас:')
    for value in arr:
        if number > arr[value]:
            print(f" {value} - {arr[value]}")

track_low_stock_with_for(products)
