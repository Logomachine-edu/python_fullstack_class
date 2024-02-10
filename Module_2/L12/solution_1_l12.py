def collect_data(data):
    return process_data(data)


def process_data(data):
    average_value = sum(data) / len(data)
    return summarize_data(average_value)


def summarize_data(average_value):
    return print(f'Среднее значение: {average_value}')

collect_data([1, 2, 3, 4, 5])
collect_data([10, 15, 5, 20])