price, visits = int(input("Введите цену:")), int(input("Введите кол-во посещений:"))
if 10 <= visits <= 19:
    total_price = price - (price * 10 / 100)
    print(f"Итоговая цена: {int(total_price)}")
elif visits >= 20:
    total_price = price - (price * 20 / 100)
    print(f"Итоговая цена: {int(total_price)}")
else:
    print(f"Итоговая цена: {int(price)}")
