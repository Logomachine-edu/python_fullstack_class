from typing import Iterator



def gen() -> Iterator[int]:
    res = []
    res.append(0)
    res.append(1)
    i = len(res)
    while i < 10:
       res.append(res[i-1]+res[i-2])
       i += 1
    print(res)

gen()
