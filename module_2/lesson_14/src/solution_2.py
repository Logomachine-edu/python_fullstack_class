from typing import Iterator
a = [99, 150, 200, 349, 501]


def gen(val) -> Iterator[int]:
    res = set(list(map(lambda x: (round(x/100) * 100), val)))
    print(res)

gen(a)
