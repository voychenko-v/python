"""
    Вводится строка.

    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""

string = input('Введите строку: ')

count_word = 0
temp = 0

for i in string:
    if i.isalnum() and temp == 0:
        count_word += 1
        temp = 1
    else:
        if i.isalnum() is False:
            temp = 0
print('Количество слов: ', count_word)


