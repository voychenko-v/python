data = [
    (2, "green"),
    (1, "blue"),
    (2, "yellow"),
    (1, "aquamarine"),
    (4, "red"),
    (3, "gold"),
    (5, "black"),
    (2, "brown"),
    (5, "pink"),
    (1, "purple"),
    (4, "white"),
    (1, "gray"),
]

data_color = sorted(data, key=lambda i: i[1])
print('Отсортированый по цвету: ', data_color)
data_color_2 = sorted(data, key=lambda i: (i[0], i[1]))
print('Отсортированый по первому елементу: ', data_color_2)
data_color_3 = (list(filter(lambda i: len(i[1]) == 4, data)))
print('Цвет из 4 букв:', data_color_3)
data_color_4 = max(data, key=lambda i: len(i[1]))
print('Цвет c найбольшим количесвом букв: ', data_color_4[1])
# 1. Вывести список data, отсортированный по цвету (2 элемент кортежа).

# 2. Отсортировать список по 1 элементу кортежа, а если значения одинаковые,
#    то их отсортировать по 2 элементу. Результат вывести на экран.

# 3. С помощью filter() и lambda вывести только те кортежи из списка,
#    цвет которых состоит из 4 букв.

# 4. Вывести цвет, которой состоит из найбольшего количества букв.
