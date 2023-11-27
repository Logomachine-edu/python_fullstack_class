#Запрашиваем список и преобразуем его в массив чисел
arr = list(map(int,input("Введите список цен через запятую:").split(",")))
positions = list(map(int,input("Введите позиции для перестановки через запятую:").split(",")))
#Заранее записываем значения и их индексы, чтобы во время смены цен не было ошибки
minimal_price = positions[0]
maximal_price = positions[1]
#Меняем минимальную цену на максимальную
arr[arr.index(minimal_price)] = maximal_price
arr[arr.index(maximal_price)] = minimal_price
#Выводим результат
print(arr)