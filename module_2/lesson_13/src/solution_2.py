import time
import random
start_time = time.time()
solution_1 = "Логотип Васильевский рынок"
solution_2 = "Макет сайта Логомашины"

def create_design (func) :
    def some_func(some_argument) :
        time.sleep(random.random()*3)
        func()
    return some_func

@create_design
def time_watcher() :
    end_time = time.time()
    expand_time = round(end_time - start_time , 4)
    return print(f"Execution: {expand_time} seconds") 

time_watcher(solution_1)


