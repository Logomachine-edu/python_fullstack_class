numbers_test = [100,200,300]
numbers_test2 = [15,23,39,50]


def sum_sales_with_for (lst):
    sum = 0
    for i in lst:
        sum += i
        
    print(*lst , sep="+" , end="=")
    print(sum)


sum_sales_with_for(numbers_test)