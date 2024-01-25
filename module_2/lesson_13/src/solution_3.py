zakaz = ("логотип" , "малый бизнес")
cashe = ()

def estimate_time(func) :
    def wrapper(*args, **kwargs):
        global cashe
        if args == cashe:
            print(f"Вернули из кэша: Цена")
        else:
            cashe = args
            print(f"Посчитали: Цена")
    return wrapper

@estimate_time
def access(*args):
    #some calculate
    return "Цена"

    
    
access(zakaz)
access(zakaz)
