data_sets = [
    (sorted([10, 23, 35, 47], key = lambda x: (x%2 == 1))),

    (sorted([5, 7, 8, 10], key = lambda x: (x > 7))),

    (sorted([1, 2, 3, 5, 6], key = lambda x: (x < 5))),

    (sorted([10, 20, 30, 40, 50], key = lambda x: (x%8 == 0 or x%8 == 0))) 
]



for data, filter_func in data_sets:
    def filter_data(data,filter_func):
        return filter_func(data)    

    filtered_data = filter_data(data, filter_func)

print(filtered_data)