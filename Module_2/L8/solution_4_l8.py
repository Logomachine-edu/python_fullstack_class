provision = {}
design = {}

for i in range(6):
    records = input('Введите через запятую: отдел, должность и фамилию нового сотрудника: ')
    division, post, name = records.split(", ")
    
    if division == 'Снабжение':
        provision[post] = name
    elif division == 'Дизайн':
        design[post] = name
        
print(f"Снабжение: {provision}")
print(f"Дизайн: {design}")