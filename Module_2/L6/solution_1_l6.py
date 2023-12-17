products = input('Введите товары через запятную: ')
odd = products.split(', ')
print('Товары с нечетным индексом:', ', '.join(odd[1::2]))