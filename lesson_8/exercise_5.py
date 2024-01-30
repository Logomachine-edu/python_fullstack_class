def store_name(products1, products2):
    f1_store = products1.difference(products2)
    f2_store = products2.difference(products1)
    print('Только в первом магазине:', ", ".join(f1_store))
    print('Только во втором магазине:', ", ".join(f2_store))


store_name({'Хлеб', 'Молоко', 'Сыр'}, {'Молоко', 'Йогурт', 'Сок'})
store_name({'Кофе', 'Чай', 'Сахар'}, {'Какао', 'Чай', 'Сгущенка'})
