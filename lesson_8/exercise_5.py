first_store_1 = {'Хлеб', 'Молоко', 'Сыр'}
second_store_1 = {'Молоко', 'Йогурт', 'Сок'}
first_store_2 = {'Кофе', 'Чай', 'Сахар'}
second_store_2 = {'Какао', 'Чай', 'Сгущенка'}
f1_store = first_store_1.difference(second_store_1)
s1_store = second_store_1.difference(first_store_1)
f2_store = first_store_2.difference(second_store_2)
s2_store = second_store_2.difference(first_store_2)
print('Только в первом магазине:', f1_store)
print('Только во втором магазине:', s1_store)
print('Только в первом магазине:', f2_store)
print('Только во втором магазине:', s2_store)
