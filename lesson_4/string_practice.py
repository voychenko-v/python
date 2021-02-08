string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'

# 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'
print('Задание №1:', string.replace(', ', ' '))

# 2. Найти индекс самой последней буквы 's' в строке.
#    Результат: 53
print('Задание №2:', string.rindex('s'))

# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6
print('Задание №3:', string.count('i'))

# 4. Найти и вывести срез строки.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов)
a = string.find('simply')
b = string.rfind('text') + 4
print('Задание №4:', string[a:b].replace(', ', ' '))

# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'
a = int(len(string) / 2)

string_1 = (string[:a].replace(', ', ' ') * 3) + string[a:].replace(', ', ' ')
print('Задание №5:', string_1)