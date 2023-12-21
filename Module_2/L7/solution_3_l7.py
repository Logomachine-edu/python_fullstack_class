number_list = list(map(int, input('Введите список: ').split(', ')))
numbers = [x for x in number_list]
n = numbers[0]
m = numbers[-1]
k = numbers[1]
print(f'Числа подсписка: {", ".join(map(str, numbers[n:m:k]))}')