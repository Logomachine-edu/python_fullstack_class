price = input('Введите цены: ')
odd = price.split(', ')
print('Цены без скидки:', ', '.join(odd[1::2]))