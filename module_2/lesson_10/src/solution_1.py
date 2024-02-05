price = int(input("Введите цену:"))
visits = int(input("Введите количество посещений:"))

def discount_calc (a: int , b: int):
    if 20 > b >= 10 : 
        result = a * 0.9
    elif b >= 20:
        result = a * 0.8
    else:
        result = a
    
    return int(result)

print("Итоговая цена:" , discount_calc(price,visits))