def change_price(function):
    def wrapper(product, new_price, price):
        changes = function(product, new_price, price)
        return changes
    return wrapper
    

@change_price
def change_price(product, new_price, price):
    print(f"Цена на {product} изменилась! {new_price} > {price}")
    return new_price
    
data = [
    change_price('Кресло', 5000, 4500),
    change_price('Стол', 8000, 7600)
]