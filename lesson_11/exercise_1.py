def sum_sales_with_for(lst):
    total = 0
    for i in range(0, len(lst)):
        total += lst[i]
    print(*lst, sep="+", end=f"={total}\n")


sum_sales_with_for([100, 200, 300])
sum_sales_with_for([15, 23, 39, 50])
