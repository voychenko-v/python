string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'

# 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'
string_1 = string.replace(', ', ' ')
print('Задание №1:', string_1)

# 2. Найти индекс самой последней буквы 's' в строке.
#    Результат: 53
string_2 = string_1.rindex('s')
print('Задание №2:', string_2)

# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6
string_3 = string_1.lower().count('i')
print('Задание №3:', string_3)

# 4. Найти и вывести срез строки.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов)
a = string_1.find('simply')
b = string_1.rfind('text') + 4
print('Задание №4:', string_1[a:b])

# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'
a = int(len(string_1) / 2)

string_4 = (string_1[:a] * 3) + string_1[a:]
print('Задание №5:', string_4)
