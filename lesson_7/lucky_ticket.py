"""
    Написать функцию, которая будет проверять счастливый билетик или нет.

    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""


def is_lucky(ticket_num):
    ticket_num = str(ticket_num)
    len_num = int(len(ticket_num) / 2)
    half_num = ticket_num[0:len_num]
    half_num_2 = ticket_num[len_num:]
    sum_1 = 0
    sum_2 = 0
    for i in half_num:
        sum_1 += int(i)
    for i in half_num_2:
        sum_2 += int(i)

    result = sum_1 == sum_2
    return result


assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True

print("All tests passed successfully!")
