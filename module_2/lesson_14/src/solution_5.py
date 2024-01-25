from collections import Counter
items_list_1 = [('Рубашка', 'Одежда'), ('Кружка', 'Посуда')]
items_list_2 = [('Рубашка', 'Одежда'), ('Штаны', 'Одежда'), ('Кружка', 'Посуда')]
items_list_3 = [('Ручка', 'Канцелярия'), ('Тетрадь', 'Канцелярия'), ('Кружка', 'Посуда'), ('Стул', 'Мебель')]

def inventory_counter(items):
    type_counts = Counter(map(lambda item: item[1], items))
    return dict(type_counts)

print(inventory_counter(items_list_1))
print(inventory_counter(items_list_2))
print(inventory_counter(items_list_3))