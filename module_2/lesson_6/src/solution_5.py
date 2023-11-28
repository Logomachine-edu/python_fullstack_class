#Запрашиваем список и преобразуем его в массив чисел
arr = list(map(int,input("Введите список цен через запятую:").split(",")))
#Меняем цены местами
arr[arr.index(max(arr))] , arr[arr.index(min(arr))] = arr[arr.index(min(arr))] , arr[arr.index(max(arr))]
#Выводим результат
print(arr)

