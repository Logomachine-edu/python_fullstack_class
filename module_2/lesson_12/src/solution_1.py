
data = [1,2,3,4,5]
numbers = [int(x) for x in data]

def collect_data(lst) :
    def   process_data(val) :
        result = sum(val) / len(val)
        return result
    def summarize_data(res):
        return print(f"Среднее значение: {int(res)}")
    return summarize_data(process_data(lst))
    
collect_data(numbers)