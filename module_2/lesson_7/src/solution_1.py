#Запрашиваем список и преобразуем его в массив 
words = list(input("Введите строку:").split(" "))
reversed_words = [item[::-1] for item in words]
joined_words = " ".join(reversed_words)
print(joined_words)
