price_1: list[int] = [50, 45, 30, 25]
price_2: list[int] = [100, 90, 85, 70, 60]

# присваиваем индексы
i, j = price_1.index(min(price_1)), price_1.index(max(price_1))
# меняем местами индексы максимального значения числа с минимальным
price_1[i], price_1[j] = price_1[j], price_1[i]

# присваиваем индексы для 2-го списка чисел
k, t = price_2.index(min(price_2)), price_2.index(max(price_2))
# меняем местами индексы максимального значения числа с минимальным
price_2[k], price_2[t] = price_2[t], price_2[k]

print(price_1)
print(price_2)
