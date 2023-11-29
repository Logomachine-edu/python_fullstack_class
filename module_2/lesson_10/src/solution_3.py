workers = {"Анна": 5,"Боб":7,"Сюзан":9}
workers_2 = {"Джон": 1,"Майк":1,"Эмили":1}

def search (a):
    max_value = max(a.values())
    result = {key:value for key , value in a.items() if value == max_value}
    return result.keys()

print("Самые ответственные сотрудники:" , search(workers_2))