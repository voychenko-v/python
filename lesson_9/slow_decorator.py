"""
    Реализовать декораторы:
    1. @time_decorator - считает и выводит время работы функции,
        если функция выполняется дольше 5 секунд, тогда дополнительно
        выводить сообщение print(f'{func.__name__} - very slow function')

    * в func.__name__ лежит название функции

    2. @slow_decorator - замедляет выполнение функции на 5 секунд

    Используйте библиотеку time, а именно функции time и sleep

"""
import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        # time.sleep(5)
        result = func(*args, **kwargs)
        end = time.time() - start
        print(end)
        if end > 5:
            print(f'{func.__name__} - very slow function')
        return result
    return wrapper


def slow_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(5)
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result
    return wrapper


@slow_decorator
@time_decorator
def sum_1(a, b):
    return print(a + b)


sum_1(44, 555)
