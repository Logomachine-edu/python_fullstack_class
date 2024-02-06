positions = [
    'Снабжение', 'Менеджер', 'Иванов',
    'Дизайн', 'Дизайнер', 'Смирнов',
    'Снабжение', 'Менеджер', 'Петров',
    'Дизайн', 'Иллюстратор', 'Сидоров',
    'Маркетинг', 'Аналитик', 'Сергеев',
    'Дизайн', 'Дизайнер', 'Васильев'
]
supply: dict = {}
design: dict = {}

"Разбиваем на 6 подсписков"
chunk_size = 3
chunks = [positions[i:i + chunk_size] for i in range(0, len(positions), chunk_size)]

for index in range(6):
    total = chunks[index]
    for i in range(3):
        if total[i] == "Снабжение":
            supply.clear()
            supply.update({total[i + 1]: total[i + 2]})
        elif total[i] == "Дизайн":
            if total[i+1] == "Дизайнер":
                design.update({total[i + 1]: total[i + 2]})
            else:
                design.update({total[i + 1]: total[i + 2]})
print(f"Снабжение: {supply}")
print(f"Дизайн: {design}")
