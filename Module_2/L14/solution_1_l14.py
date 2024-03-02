def grey_shades(num):
    return [(i, i, i) for i in range(0, num, 5)]
    
print(grey_shades(250))