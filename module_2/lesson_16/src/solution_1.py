quantity = int(input("Введите количество полок:"))
longs_arr = list(input("Введите длины полок через запятую:").split(","))
longs = [int(x) for x in longs_arr]

a = [[longs[i], 0] for i in range(quantity)]
print(a)

