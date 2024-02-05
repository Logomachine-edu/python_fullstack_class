#Запрашиваем вводное слово
logo = str(input("Введите название компании:"))
#Считаем количество символов и разделяем
a = len(logo)
first_half = logo[int(a / 2):] 
second_half = logo[:int(a / 2)]
#Выводим свапнутое название
print(first_half + second_half)