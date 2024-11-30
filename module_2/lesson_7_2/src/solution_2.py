list_of_numbers = input('Введите список: ').split(',')

summa = 0

for i in map(int, list_of_numbers[1:4]):
    summa += i

print(f'Сумма подсписка: {summa}')