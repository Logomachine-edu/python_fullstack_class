quantity = int(input("Введите количество полок:"))
longs_arr = list(input("Введите продажи по товарам:").split(";"))
longs_str = [list(map(int, x.split(","))) for x in longs_arr] # [['2', '3', '4'], ['2', '3', '4']]

print(longs_str)

