def round_price(price):
    rounded_price = list(dict.fromkeys(map(lambda x: round(x, -2), price)))
    return rounded_price
    
print(round_price([99, 150, 200, 349, 501]))