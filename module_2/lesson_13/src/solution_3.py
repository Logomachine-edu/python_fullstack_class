zakaz = ("логотип" , "малый бизнес")
cashe = ()

def estimate_time(func) :
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@estimate_time
def access(*args):
    global cashe
    if args == cashe:
        return print(f"Вернули из кэша: Цена")
    else:
        cashe = args
        return print(f"Посчитали: Цена")
    
    
access(zakaz)
access(zakaz)
