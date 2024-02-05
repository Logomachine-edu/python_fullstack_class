
prices = list(input("Введите цены через запятую:").split(","))
prices_numbers = [int(x) for x in prices]

def calculate_discount (some_list:list) -> int:   
    discount: int = some_list[-1]
    some_list.pop()
    result : int = sum(some_list) / discount
    return result


print(calculate_discount(prices_numbers))
