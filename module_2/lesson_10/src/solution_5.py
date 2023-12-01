klicks = list(input("Введите клики, показы и просмотры через запятую:").split(","))
klicks_numbers = [int(x) for x in klicks]

def analyze_ad_efficiency (data):
    if data[0]/data[1] < 0.01 and data[2] > data[1]:
        result = "Недооцененная"
    elif 0.01 <= data[0]/data[1] <= 0.05:
        result = "Низкая"
    elif 0.05 < data[0]/data[1] <= 0.1 and data[2] > data[0]:
        result = "Средняя"
    elif 0.1 < data[0]/data[1]:
        result = "Высокая"
    else:
        result = "Неопределенная"

    return result

print("Эффективность:", analyze_ad_efficiency(klicks_numbers))
