import time
import random

solution_1 = "Логотип Васильевский рынок"
solution_2 = "Макет сайта Логомашины"

def create_design (func) :
    def some_func(*args, **kwargs) :
        start_time = time.time()        
        func()
        end_time = time.time()
        expand_time = round(end_time - start_time , 4)
        print(f"Execution: {expand_time} seconds") 
    return some_func

@create_design
def time_watcher() :
    time.sleep(random.random()*3) 
time_watcher(solution_1)


