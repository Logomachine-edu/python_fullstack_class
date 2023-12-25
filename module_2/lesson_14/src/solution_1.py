from typing import Iterator

def gen() -> Iterator[int]:
    res = []
    for x in range(51):
        if x == 0 or x % 5 == 0:
            a = (x,x,x)
            res.append(a)
    return print(res)

gen()
