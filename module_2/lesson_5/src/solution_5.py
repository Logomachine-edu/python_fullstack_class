#Запрашиваем вводное описание
logo = str(input("Введите описание:"))
#Приводим к нижнему регистру, чтобы избежать ошибок при вводе
logo_lower = logo.lower()
#Ищем и выводим
print(logo_lower.replace("design","art", 2))