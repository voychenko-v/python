"""
    Пользователь вводит количество студентов N.
    После чего вводит N строк, в которых записана фамилия и балл через пробел.

    Программа выводит список фамилий, отсортированный по их баллам по убыванию.

    Пример:

    [out] Введите количество студентов:
    [in]  3

    [out] Введите фамилию и балл:
    [in]  Иванов 87

    [out] Введите фамилию и балл:
    [in]  Смирнов 90

    [out] Введите фамилию и балл:
    [in]  Фролов 89

    [out]
        1. Смирнов
        2. Фролов
        3. Иванов
"""


def main():
    while True:
        list_student = []
        num_string = int(input('Введите количество студентов: '))
        while 0 < num_string:
            list_student.append(input().split(' '))
            num_string -= 1
        list_student_sort = sorted(list_student, key=lambda x: x[1], reverse=True)
        for i in list_student_sort:
            print(f'{list_student_sort.index(i) + 1}. {i[0]} {i[1]}')
        if input('Continue ? (Y/n) ') == 'n':
            print('Bye')
        break
    return


if __name__ == "__main__":
    main()


main()
