def employees_task(lst):
    max_key = max(lst.values())
    goods_max = [key for key in lst if lst[key] == max_key]
    print("Самый ответственный:", ", ".join(goods_max))


employees_task({
    "Анна": 5,
    "Боб": 7,
    "Сюзан": 9
})
employees_task({
    "Джон": 1,
    "Майк": 1,
    "Эмили": 1
})
