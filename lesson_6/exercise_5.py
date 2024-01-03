def swapping_min_max(price):
    index_max = price.index(max(price))
    index_min = price.index(min(price))
    price[index_max], price[index_min] = price[index_min], price[index_max]
    print(price)


swapping_min_max([50, 45, 30, 25])
swapping_min_max([100, 90, 85, 70, 60])
