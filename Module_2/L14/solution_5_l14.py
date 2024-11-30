from collections import Counter

def inventory(products):
    type_products = Counter(map(lambda product: product[1], products))
    return dict(type_products)
    
    
print(inventory([('Рубашка', 'Одежда'), ('Кружка', 'Посуда')]))
print(inventory([('Рубашка', 'Одежда'), ('Штаны', 'Одежда'), ('Кружка', 'Посуда')]))
print(inventory([('Ручка', 'Канцелярия'), ('Тетрадь', 'Канцелярия'), ('Кружка', 'Посуда'), ('Стул', 'Мебель')]))