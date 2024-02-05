products_1 = [[4, 2], [5, 3], [6, 5]]
products_2 = [[3, 1], [4, 4]]


def func(lst):
    for i in range(len(lst)):
        a = [[lst[i][-1] * (i + 1)] * lst[i][-1] for i in range(len(lst))]

    print(a)


func(products_1)
func(products_2)
