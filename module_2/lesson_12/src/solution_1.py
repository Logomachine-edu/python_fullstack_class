import statistics
data = [1, 2, 3, 4, 5]

def collect_data(lst) :
    def   process_data(val) :
        return statistics.mean(val)
    def summarize_data(res):
        return print(f"Среднее значение: {res}")
    return summarize_data(process_data(lst))
    
collect_data(data)