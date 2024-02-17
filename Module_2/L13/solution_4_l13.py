def assessment(function):
    def wrapper(input_info):
        if len(input_info) == 2:
            if isinstance(input_info[0], str) and isinstance(input_info[1], int):
                print('Estimated time calculated successfully!')
            elif not isinstance(input_info[0], str):
                print('Ошибка: Первый аргумент не строка!')
            elif not isinstance(input_info[1], int):
                print('Ошибка: Второй аргумент не число!')
        function()
    return wrapper

@assessment
def estimate_time() -> None:
    pass
    
input_info = [
    estimate_time(('Веб-сайт', 'пять')),    
    estimate_time(('Визитка', 10))
]