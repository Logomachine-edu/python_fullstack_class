from typing import Iterator
a = [99, 150, 200, 349, 501] 

def round100(n):
    res = []
    for i in n:
        res.append(round(i/100)*100)
    return print(res)


round100(a)