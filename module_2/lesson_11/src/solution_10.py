days = int(input("Введите количество дней в месяце:"))

def sales_schedule_with_range (day):
    discount_days = []
    for i in range(1,day + 1,3):
        discount_days.append(i)
    
    return print(f"Дни распродаж: {discount_days}")


sales_schedule_with_range(days)