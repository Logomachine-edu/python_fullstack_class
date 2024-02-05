time = int(input("Который час?:"))

def theme_calc (a):
    if 6 >= a > 18:
        result = "Светлый"
    else:
        result = "Тёмный"
    return result

print("Текущий цвет темы:" , theme_calc(time))