#Запрашиваем список и преобразуем его в массив чисел
arr = list(input("Введите строку:").split(","))
arr_numbers = [int(item) for item in arr]
n = arr_numbers[0]
m = arr_numbers[-1]
k = arr_numbers[1]
print(arr_numbers[n:m:k])
