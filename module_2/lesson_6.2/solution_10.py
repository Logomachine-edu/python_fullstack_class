price = 1

price_list = []

while price != 0:
    price = float(input("Введите цену на товар(ноль закончит ввод): "))
    if price != 0:
        price_list.append(price)

average_price = sum(price_list) / (len(price_list))
    
print(f"Средняя цена товаров состовляет {round(average_price, 2)}")


#Задание 10: Расчет средней стоимости товаров 🔥
#Описание:

#Роман хочет знать среднюю стоимость товаров на полке. 
#Программа должна вычислять и выводить среднюю цену товаров.