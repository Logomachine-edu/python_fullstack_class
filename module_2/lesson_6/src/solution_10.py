#Запрашиваем список и преобразуем его в массив чисел
arr = list(input("Введите список цен через запятую:").split(","))
arr_numbers = [int(x) for x in arr]
#Считаем средн
arr_sort = sum(arr_numbers) / len(arr_numbers)
#Выводим результат
print("Средняя цена", arr_sort)
