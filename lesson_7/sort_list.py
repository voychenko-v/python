"""
    Напишите функцию, которая принимает список чисел
    и возвращает отсортированный список,
    при условии, что все числа -1 остаются на своих местах.

    [in]   [6, 3, -1, 4, 2, -1, 1]
    [out]  [1, 2, -1, 3, 4, -1, 6]
"""


def sort_ascending(x):
    num_list = []
    final_list = []
    index_num = 0
    for i in x:
        if i > 0:
            num_list.append(i)
    num_list = sorted(num_list)
    for i in x:
        if i != -1:
            final_list.append(num_list[index_num])
            index_num += 1
        elif i == -1:
            final_list.append(-1)
    return final_list



t_1 = [-1, 150, 190, 170, -1, -1, 160, 180]
assert sort_ascending(t_1) == [-1, 150, 160, 170, -1, -1, 180, 190]

t_2 = [-1, -1, -1, -1, -1]
assert sort_ascending(t_2) == [-1, -1, -1, -1, -1]

t_3 = [4, 2, 9, 11, 2, 16]
assert sort_ascending(t_3) == [2, 2, 4, 9, 11, 16]

t_4 = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
assert sort_ascending(t_4) == [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]

t_5 = [-1]
assert sort_ascending(t_5) == [-1]

print("All tests passed successfully!")
