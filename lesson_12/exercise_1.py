import statistics


def collect_data(data):
    return process_data(data)


def process_data(data):
    average = statistics.mean(data)
    return summarize_data(average)


def summarize_data(average):
    return print(f"Итог: Среднее значение: {average}")


collect_data([1, 2, 3, 4, 5])
collect_data([10, 15, 5, 20])
