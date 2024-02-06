def sum_sales_with_for(prices):
    prices_sum = 0
    
    for i in range(len(prices)):
        prices_sum += prices[i]
        
    print("Сумма продаж: ", end = '')
    print(*prices, sep='+', end='=')
    print(prices_sum)
    
sum_sales_with_for([100, 200, 300])
sum_sales_with_for([15, 23, 39, 50])