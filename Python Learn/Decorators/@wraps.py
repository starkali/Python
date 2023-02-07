# 1) Определяем функцию `print_function_data`
# 2) Внутри `print_function_data` определяем вспомогательную функцию `wrapper`
# 3) Функция `wrapper` печатает имя функции, которая была передана как аргумент в `print_function_data`, используя `function.__name__`
# 4) Функция `wrapper` также печатает документацию функции, используя `function.__doc__`
# 5) Затем `wrapper` вызывает функцию, переданную как аргумент, с использованием `*args` и `**kwargs` для передачи любых аргументов в функцию.
# 6) Функция `print_function_data` возвращает `wrapper`
# 7) Затем мы определяем функцию `squares_sum`, которая вычисляет сумму квадратов двух чисел.
# 8) Мы используем декоратор `@print_function_data`, чтобы показать, что мы хотим использовать `print_function_data` с `squares_sum`
# 9) Наконец, мы вызываем функцию `squares_sum` с аргументами `2` и `3`, и печатаем результат.

from functools import wraps
def print_function_data(function):
    """
    This is decorator function
    :param function:
    :return:
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are using {function.__name__}")
        print(f"Function documentation {function.__doc__}")
        return function(*args, **kwargs)
    return wrapper


@print_function_data
def squares_sum(a, b):
    """

    :param a: first number
    :param b: second number
    :return: sum of squares first and second numbers: (a * a + b * b)
    """
    return a * a + b * b


# print(squares_sum(2, 3))
print(squares_sum.__doc__)
print(squares_sum.__name__)
help(squares_sum)