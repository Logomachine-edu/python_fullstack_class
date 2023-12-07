data_sets = [
    ([10, 23, 35, 47], lambda x: (x%2 == 1)),

    ([5, 7, 8, 10], lambda x: (x > 7)),

    ([1, 2, 3, 5, 6], lambda x: (x < 5)),

    ([10, 20, 30, 40, 50], lambda x: (x%8 == 0 and x%5 == 0))
]

def filter_data(data,filter_func):
    filtered_data = list(filter(filter_func , data))
    return print(f'Отфильтрованные данные: {filtered_data}')


for data, filter_func in data_sets:
    filter_data(data, filter_func)
