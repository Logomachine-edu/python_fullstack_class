words: dict = {'Красивый': 'Прекрасный', 'Уродливый': 'Некрасивый', 'Сложный': 'Запутанный', 'Простой': 'Легкий'}
print("Синоним:", words['Красивый'])
print("Синоним:", words['Уродливый'])
print("Синоним:", words['Сложный'])
print("Синоним:", words['Простой'])

"Проверка на ошибку с добавлением в список новых синонимов"
examination = input("Введите слово для проверки:")
if examination not in words.keys():
    print("Данного слова нет наличии")
    words["new_key"] = examination
    new_word = input("Введите для этого слова синоним:")
    words[examination] = new_word
    del words["new_key"]
    print("Пример добавление в список новых синонимов:", words)
else:
    print("Синоним:", words[examination])
