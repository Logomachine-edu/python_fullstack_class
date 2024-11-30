def assessment(function):
    def wrapper(name, tasks, *args, **kwargs):
        if len(args) != 0 or len(kwargs) != 0:
            print('Ошибка: Неправильное количество аргументов!')
            
        if isinstance(name, str) and isinstance(tasks, int):
            print('Estimated time calculated successfully!')
            
        if not isinstance(name, str):
            print('Ошибка: Первый аргумент не строка!')
            
        if not isinstance(tasks, int):
            print('Ошибка: Второй аргумент не число!')
        
        function(name, tasks)
    return wrapper

@assessment
def estimate_time(name, tasks):
    return assessment
    

estimate_time('Веб-сайт', 'пять')    
estimate_time('Визитка', 10)