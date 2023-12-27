user_1 = ("Роман" , "correctpassword")
user_2 = ("Витя" , "nocorrectpassword")


def access_client_data(func) :
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@access_client_data
def access(*args):
    if args[0] == "Роман" and args[1] == "correctpassword" :
        return print(f"Доступ получен. Данные:...")
    else:
        return print(f"В доступе отказано!")
    
access(*user_1)
access(*user_2)



