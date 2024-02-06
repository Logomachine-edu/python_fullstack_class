def mas_digital(digital):
    n = digital[0]
    m = digital[-1]
    k = digital[1]
    new_digital = [str(k) for k in digital[n:m:k]]
    print(f"Числа подcписка: {', '.join(new_digital)}")


mas_digital([1, 2, 3, 4, 5])
mas_digital([2, 1, 6])
