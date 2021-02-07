"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.

    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)

    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))

    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "some string".
        Результат: "some edited string".
    (Использовать форматирование строк f либо метод format)
"""

# можно заменить данную строку на input()
string = 'Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY.'

#1
up = 0
low = 0

for i in string:
    if i.isupper():
        up += 1
    elif i.islower():
        low += 1
if up > low:
    string_1 = string.upper()
elif up < low:
    string_1 = string.lower()
else:
    string_1 = string.swapcase()
print(
    'Задание №1\n'
    f'Исходная строка: {string}\n'
    f'Результат: {string_1}\n'
)

#2
if string.istitle():
    string_2 = 'done. ' + string
else:
    string_2 = string.replace(string[0:6], 'draft: ')
print(
    'Задание №2\n'
    f'Исходная строка: {string}\n'
    f'Результат: {string_2}\n'
)

#3
if len(string) > 20:
    string_3 = string[0:20]
else:
    string_3 = string.ljust(20, '@')
print(
    'Задание №3\n'
    f'Исходная строка: {string}\n'
    f'Результат: {string_3}\n'
)
