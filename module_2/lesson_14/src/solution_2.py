from typing import Iterator
a = [99, 150, 200, 349, 501]


def gen(val) -> Iterator[int]:
    res = []
    for x in val:
       res.append(round(x/100) * 100)
    print(res)

gen(a)
