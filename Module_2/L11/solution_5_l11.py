def sales_schedule_with_range(days):
    sale_days = []
    for i in range(3, days + 1, 3):
        sale_days.append(i)
    print(f"Дни распродаж: {sale_days}")

sales_schedule_with_range(30)
sales_schedule_with_range(31)