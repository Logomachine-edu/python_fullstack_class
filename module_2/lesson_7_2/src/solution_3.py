list_of_numbers = list(map(int, input('Введите список: ' ).split(',')))

k = list_of_numbers[1]
n = list_of_numbers[0]
m = list_of_numbers[-1]

print(f'Числа подсписка: {list_of_numbers[n:m:k]}')