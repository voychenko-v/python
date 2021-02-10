"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)

    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)


    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""  # noqa: E501

import random
import string


def lite_password():
    password_l = ''
    while len(password_l) < 9:
        i = random.choice(string.ascii_lowercase)
        password_l += i
    print('Ваш пароль: ', password_l)
    return


def mid_password():
    password_m = ''
    while len(password_m) < 9:
        i = random.choice(string.ascii_letters + string.digits)
        password_m += i
    if password_m.islower() and password_m.isupper() and password_m.isdigit() is False:
        return mid_password()
    print('Ваш пароль: ', password_m)
    return


def hard_password():
    password_h = ''
    random_num = random.randint(8, 17)
    while len(password_h) < random_num:
        i = random.choice(string.ascii_letters + string.digits + string.punctuation)
        password_h += i
    if password_h.islower() and password_h.isupper() and password_h.isdigit() is False:
        return hard_password()
    print('Ваш пароль: ', password_h)
    return


def main():
    password = input(
        'Выбирете вариант пароля: \n'
        '1. Простой пароль\n'
        '2. Средний пароль\n'
        '3. Сложний пароль\n'
        'Выбор: '
    )
    if password == '1':
        lite_password()
    elif password == '2':
        mid_password()
    elif password == '3':
        hard_password()
    else:
        print('Введите число от 1 до 4')
        return main()
    return


if __name__ == '__main__':
    main()







