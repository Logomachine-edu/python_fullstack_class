#Обьявляем сотрудников в переменные
workers = ["Света","Маша","Олег","Паша"]
workers_even = workers[::2]
workers_odd = workers[1::2]
#Выводим на табло
print("В чётные дни работают:", ", ".join(workers_even), "\n \n" ,"В нечётные дни работают:", ", ".join(workers_odd))
