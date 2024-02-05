price_1 = ("Кресло", 5000, 4500)
price_2 = ("Стол", 8000, 7600)

def swap_price (price) :
    return print(f'Цена на {price[0]} изменилась! {price[1]} > {price[2]}')

swap_price(price_2)
swap_price(price_1)