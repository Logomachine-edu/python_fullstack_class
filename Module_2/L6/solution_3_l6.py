products = input('Введите товары через запятную: ').split(', ')
check = 'Молоко'
result = check in products
print('В товарах есть молоко:', result)