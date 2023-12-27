from typing import Iterator

a = ["Стр 1","Стр 2","Стр 3"]

def gen(some_list) -> Iterator[int]:
    return print((i * i for i in some_list))

gen(a)