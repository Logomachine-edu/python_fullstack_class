price = input("Введите цены: ").split(',')
print(f"Цены без скидок: {','.join(price[1::2])}")