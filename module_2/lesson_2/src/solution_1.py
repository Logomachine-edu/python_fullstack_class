# запрашиваем у пользователя строку
number_str = input("Введите число(строка):")
# преобразуем строку в целое число
number_true = int(number_str)
#умножаем на два
number_double = number_true*2
#преобразуем в формат строки и выводим
print(str(number_double))

# Оно же, но в одну строку
#number_str = str(2*int(input("Введите число:")))
#print(type(number_str))