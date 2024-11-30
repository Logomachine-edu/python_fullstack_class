def fib_prices(value):
    fib_1, fib_2 = 0, 1
    for i in range(value):
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2 
        
for f_price in fib_prices(15):
    print(f_price, end = ", ")