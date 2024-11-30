def calculate_price(price, visits):
    
    
    if 10 <= visits < 20:
      discount_price = int(price - (price * 10 / 100))
      print(f"Итоговая цена: {discount_price}")
    elif 20 <= visits:
      discount_price = int(price - (price * 20 / 100))
      print(f"Итоговая цена: {discount_price}")
    else:
      print(f"Итоговая цена: {price}")
      
calculate_price(100, 5)
calculate_price(200, 10)
calculate_price(150, 20)