product_list_1 = ['fruit', 'toy', 'fruit', 'toy']
product_1 = 'toy'

product_list_2 = ['clothes', 'clothes', 'clothes']
product_2 = 'clothes'


def count_specific_items_with_while(product, product_list):
    while product in product_list:
        product_all = product_list.count(product)
        print(f"Количество {product}: {product_all}")
        break


count_specific_items_with_while(product_1, product_list_1)
count_specific_items_with_while(product_2, product_list_2)
