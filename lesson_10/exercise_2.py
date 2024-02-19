while True:
    digital = int(input("Текущее время:"))
    if 6 <= digital < 18:
        print("Цвет фона: Светлый")
        break
    elif 0 <= digital <= 18:
        print("Цвет фона: Темный")
        break
    else:
        print("Введите число от 0 до 23:")
