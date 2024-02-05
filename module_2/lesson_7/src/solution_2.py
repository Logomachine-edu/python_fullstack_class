#Запрашиваем список и преобразуем его в массив чисел
arr = list(input("Введите строку:").split(","))
arr_numbers = [int(item) for item in arr]
needs_numbers = arr_numbers[1:4]
print(sum(needs_numbers))
