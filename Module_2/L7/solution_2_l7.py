number_list = list(map(int, input('Введите список: ').split(', ')))
numbers = [x for x in number_list]
print(f'Сумма подсписка: {sum(numbers[1:4])}')