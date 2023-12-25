from functools import wraps

zakaz = ("логотип" , "малый бизнес")
cashe = ()

def estimate_time(func) :
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@estimate_time
def access(val):
    global cashe
    if val == cashe:
        return print(f"Вернули из кэша: Цена")
    else:
        cashe = val
        return print(f"Посчитали: Цена")
    
    
access(zakaz)
access(zakaz)
