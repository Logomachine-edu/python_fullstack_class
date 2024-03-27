line = input('Введите строку: ').split()

new_line = []

for i in line:
    new_line.append(i[::-1])

print(" ".join(new_line))