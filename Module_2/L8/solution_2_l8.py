words = {'Красивый': 'Прекрасный', 'Уродливый': 'Некрасивый', 'Сложный': 'Запутанный', 'Простой': 'Легкий'}
word = input('Введите слово: ')

if word in words:
    print('Синоним:', words[word])
elif word in words.values():
    for first in (words.keys()):
        if words[first] == word:
            print('Синоним:', first)
else:
    print('Данного слова нет в списке.')