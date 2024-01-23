goods: dict = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
print("Цена:", goods['Яблоко'], "руб.")
print("Цена:", goods['Банан'], "руб.")
print("Цена:", goods['Кофе'], "руб.")
print("Цена:", goods['Чай'], "руб.")

"Проверка на ошибку с добавлением в список новых товаров"
examination = input("Введите слово для проверки:")
if examination not in goods.keys():
    print("Данного товара нет в наличии")
else:
    print("Цена:", goods[examination], "руб.")
