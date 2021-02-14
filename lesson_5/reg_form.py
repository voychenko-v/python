"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.

    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)

    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер

    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.

    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа

    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.

    Программа выводит сообщение:

    Поздравляем с успешной регистрацией!
    Ваш номер телефона: +380501234567
    Ваш email: example@mail.com
    Ваш пароль: ********** (кол-во  == кол-ву символов пароля)

"""


def number_phone():
    num_phone = input('Введте Ваш телефон: ')
    phone_n = ''
    for i in num_phone:
        if i.isdigit():
            phone_n += i
    if len(phone_n) < 8:
        print('Повторите ввод, Вы ввели недостаточно цифр!')
        return number_phone()
    elif len(phone_n) >= 9:
        phone_n = '380' + phone_n[-9:]
    return phone_n


def email_form():
    email_f = input('Введте Вашу емейл: ')
    if len(email_f) < 6 or email_f.count('@') != 1:
        print('Введите емейл правильно')
        return email_form()
    return email_f


def password():
    password_i = input('Введите пароль: ')
    if len(password_i) < 7 or password_i.isspace() is False:
        if password_i.isupper() or password_i.islower() or password_i.isdigit() is True:
            print('В пароле не должно быть пробелов, минимум одна буква в нижнем регистре, '
                  'одна буква в верхнем регистре и одна цыфра. Введите пароль еще раз.')
            return password()
    else:
        print('Пароль подходит')

    password_i2 = input('Введите пароль еще раз для подтверждения: ')
    if password_i != password_i2:
        print('Пароли не савпадают!')
        return password()
    else:
        password_print = len(password_i) * '*'
        return password_print


def main():
    number_final = number_phone()
    email_final = email_form()
    password_final = password()

    print(
          f'\nПоздравляем с успешной регистрацией!\n'
          f'Ваш номер телефона: {number_final}\n'
          f'Ваш email: {email_final}\n'
          f'Ваш пароль: {password_final}\n'
    )


if __name__ == '__main__':
    main()