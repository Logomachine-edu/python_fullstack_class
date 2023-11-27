#Запрашиваем список и преобразуем его в массив чисел
arr = list(map(int,input("Введите список цен через запятую:").split(",")))
#Заранее записываем значения и их индексы, чтобы во время смены цен не было ошибки
minimal_price = min(arr)
maximal_price = max(arr)
maximal_index = arr.index(max(arr))
#Меняем минимальную цену на максимальную
arr[arr.index(min(arr))] = max(arr)
#Меняем максимальную цену на заранее записанную минимальную
arr[int(maximal_index)] = minimal_price
#Выводим результат
print(arr)

