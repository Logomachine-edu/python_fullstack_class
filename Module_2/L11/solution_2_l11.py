def count_specific_items_with_while(goods, product):
    count_product = 0
    i = 0
    while i < len(goods):
        if goods[i] == product:
            count_product += 1
        i += 1 
    print(f"Количество '{product}': {count_product}")
    
count_specific_items_with_while(['fruit', 'toy', 'fruit', 'toy'], 'toy')
count_specific_items_with_while(['clothes', 'clothes', 'clothes'], 'clothes')