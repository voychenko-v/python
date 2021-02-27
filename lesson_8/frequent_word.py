"""
    Реализуйте функцию, которая принимает текст и возвращает слово, которое
    в этом тексте встречается чаще всего.

    Напишите несколько тестов для функции.

    # Если таких слов несколько - приоритет у первого, если расположить список
    # в алфавитном порядке.
    # Например:
    text = "hi world, hi python. i am very cool but i am still learning."
    # чаще всего встречаются "hi", "i" и "am", но по алфавиту "am" - раньше
    assert frequent_word(text) == "am"

"""

# "hi world, hi python. i am very cool but i am still learning"


def frequent_word(text):
    text = text.lower() + "."
    word = ""
    my_dict = {}
    for i in text:
        if i.isalpha():
            word += i
        elif i.isalpha() is False and word != "":
            if word in my_dict:
                my_dict[word] += 1
            else:
                my_dict[word] = 1
            word = ""
        elif i.isalpha() is False and word == "":
            continue

    max_value = 1
    for value in my_dict.values():
        if value > max_value:
            max_value = value

    max_key = ""
    for key, value in my_dict.items():
        if value == max_value and max_key == "":
            max_key = key
        elif value == max_value and max_key > key:
            max_key = key

    print(my_dict)
    print(max_key)
    return max_key


frequent_word("hi world, hi python. i am very cool but i am still learning")

assert frequent_word("bum, lab, set- get/ ram+ lab alf bum") == "bum"

assert frequent_word("?Bum, lab, set- get/ ram+ lab alf bum") == "bum"

assert frequent_word("?Bum, lab, set- get/ Lab ram+ lab alf bum") == "lab"

