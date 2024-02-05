category = ['fruit', 'toy', 'fruit', 'toy']
category_2 = ['clothes', 'clothes', 'clothes', 'clothes']

def count_specific_items_with_while(lst):
    item = str(input("Введите категорию для поиска:"))
    i = 0 
    result = 0
    while i < len(lst):
        if lst[i] == item : 
            result += 1
            i += 1
        else: i += 1 
    return print(f"Количество {item} : {result}")

count_specific_items_with_while(category_2)