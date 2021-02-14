"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой
"""

"""
    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран
"""

"""
    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt
"""

"""
    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое
"""

"""
    5.
    В средину файла file_practice.txt вставить строку " *some inserted text* "
    (средина - имеется в виду средина текста)
"""

with open('file_practice.txt', 'w') as f:
    # f.write('Starting practice with files\n')
    print('Starting practice with files', file=f)

with open('file_practice.txt', 'r') as f:
    print(f.read(5).upper())
    f.seek(0)
    print(f.read())

with open('files/text.txt', 'r+') as f:
    text_all = f.read()
    text_i = int(text_all.count('i'))
    text_e = int(text_all.count('e'))
    if text_i > text_e:
        text_format = text_all.replace('e', 'i')
    elif text_i < text_e:
        text_format = text_all.replace('i', 'e')
    else:
        pass
    with open('file_practice.txt', 'a') as f_2:
        print(text_format, file=f_2)

with open('file_practice.txt', 'r+') as f:
    even = len(f.read())
    if even % 2 == 0:
        print('the end', file=f)
    else:
        print('bye', file=f)
    f.seek(0)
    print(f.read())

with open('file_practice.txt', 'r') as f:
    count_text_half = len(f.read()) / 2
    f.seek(0)
    half_text = f.read(int(count_text_half))
    half_text_2 = f.read()
    with open('file_practice.txt', 'w+') as f_2:
        print(half_text, ' *some inserted text* ', half_text_2, file=f_2)


'''
    with open('file_practice.txt', 'r') as f:
    f.seek(0)
    print(f.read())
'''
