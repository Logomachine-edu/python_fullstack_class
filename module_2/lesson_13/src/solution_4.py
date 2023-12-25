user_1 = ("Сайт" , "пять")
user_2 = ("Визитка" , 10)


def estimate_time(func) :
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@estimate_time
def access(dict):
    if type(dict[1]) == int:
        return print(f"Estimated time calculated succsessfully!")
    else:
        return print(f"Второй аргумент - не число")
    
access(user_1)
access(user_2)