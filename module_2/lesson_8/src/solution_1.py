price_list: dict[str , int] =  {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
item = str(input("Введите товар:"))
print("Цена товара", item, "-" , price_list[item] , "рублей")