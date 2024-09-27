words: dict = {'Красивый': 'Прекрасный', 'Уродливый': 'Некрасивый', 'Сложный': 'Запутанный', 'Простой': 'Легкий'}
print("Синоним:", words['Красивый'])
print("Синоним:", words['Уродливый'])
print("Синоним:", words['Сложный'])
print("Синоним:", words['Простой'])

"Проверка на ошибку с добавлением в список новых синонимов"
examination = input("Введите слово для проверки:")
for k, v in words.items():
    if examination == v:
        print(k)
        break
    elif examination == k:
        print(v)
        break
    elif examination not in words.keys():
        print("Данного слова нет наличии")
        words["new_key"] = examination
        new_word = input("Введите для этого слова синоним:")
        words[examination] = new_word
        del words["new_key"]
        print("Пример добавление в список новых синонимов:", words)
