count = 0
supply: dict[str, str]  = dict() #Отдел снабжения
design: dict[str, str] = dict() #Отдел дизайна

while count < 6:
    departament, post, surname = input('Введите отдел, должность и фамилию: ').split(', ')
    count += 1

    if departament == 'Снабжение':
        supply.clear()
        supply.update({post: surname})
    elif departament == 'Дизайн':
        design.clear()
        design.update({post: surname})
    else:
        continue

print(f'Снабжение: {supply}')
print(f'Дизайн: {design}')

"""
Час бился над тем, что не мог понять, как мне сделать так, чтобы Иллюстратора не уволили.
Но я так и не понял, так что могу предположить, что иллюстратор в команду 'Дизайна' не нужен)))
"""