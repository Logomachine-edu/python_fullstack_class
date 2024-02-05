from typing import Iterator
def gen() -> Iterator[int]:
    res = []
    res.append(0)
    res.append(1)
    while True:
        i = len(res)
        yield res.append(res[i-1]+res[i-2])
print(gen())
