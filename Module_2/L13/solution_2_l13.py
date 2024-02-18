import time
 
def create_design(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        print(f"'Execution: {end_time - start_time:.2f} seconds'")
    return wrapper
 
@create_design
def create_design(design, delay):
    time.sleep(delay)
    print(design)
 
design = [
    create_design('Логотип Васильевский рынок', 2.45),
    create_design('Макет сайта Логомашины', 4.30)
]