def most_responsible(staff):
    
    
    names = list(staff.keys())
    tasks = list(staff.values())
    max_done = max(tasks)
    
    most_responsible = [name for name, complited in staff.items() if complited == max_done]
    return ', '.join(map(str, most_responsible))
    

staff = {'Анна': 5, 'Боб': 7, 'Сюзан': 9}
print(f"Самый ответственный: {most_responsible(staff)}")