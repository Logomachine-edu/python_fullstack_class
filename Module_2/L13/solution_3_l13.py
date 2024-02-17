cache = {
    'args': None,
    'result': None
}

def cache_check(func):
    def wrapper(*args):
        if cache['args'] == args:
            print(f"'Загрузили из кэша: {cache['result']}'")
        else:
            result = func(*args)
            cache['args'] = args
            cache['result'] = result
            print(f"'Посчитали цену: {result}'")
    return wrapper
        
@cache_check
def calculate_project_cost(*args):
    return 3000

cache_input = [
    calculate_project_cost('Логотип', 'малый бизнес'),
    calculate_project_cost('Логотип', 'малый бизнес')
]