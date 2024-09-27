def sales_schedule_with_range(days_in_a_month):
    total = []
    for i in range(3, days_in_a_month + 1, 3):
        total.append(i)
    print(f"Дни распродаж: {total}")


sales_schedule_with_range(30)
sales_schedule_with_range(31)
