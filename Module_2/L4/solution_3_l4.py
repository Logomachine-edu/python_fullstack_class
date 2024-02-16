usd, rub = input('Введите цену в долларах: '), input('Введите текущий курс доллара: ')
price = str(round(float(usd) * float(rub), 1))
print('Цена в рублях: ', price)