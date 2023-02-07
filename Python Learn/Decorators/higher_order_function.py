# Higher order functions, which accept another functions as arguments


# def product(n, func):
#     result = 1
#     for number in range(1, n):
#         result *= func(number)
#     return result
#
#
# def square(x):
#     return x * x
#
#
# def cube(x):
#     return x * x * x
#
#
# print(product(4, square))
# # 1 2 3
# # 1 4 9
#
# print(product(4, cube))
# # 1 2 3
# # 1 8 27

# -- 1) Определение функции product: Эта функция принимает два параметра n и func, где n - это целое число, а func - это функция.
# -- 2) Переменная result: Определена переменная result с начальным значением 1.
# -- 3) Цикл for: Цикл for итерируется по диапазону (1, n), и в каждой итерации number устанавливается в каждое значение в диапазоне.
# -- 4) Расчет result: В каждой итерации рассчитывается результат вызова func с number в качестве аргумента и сохраняется в result. Затем результат функции умножается на предыдущее значение result.
# -- 5) Инструкция return: После цикла for финальное значение result возвращается.
# -- 6) Определение функции square: Эта функция принимает аргумент x и возвращает его квадрат (x * x).
# -- 7 )Инструкция print: Вызывается функция product с 4 в качестве первого аргумента и square в качестве второго аргумента. Результат выводится в консоль.
# Ожидаемый выход кода - 8, который является произведением квадратов целых чисел от 1 до 3.


# def my_function(a, b, func):
#     result = func([a, b])
#     return result
#
#
# print(my_function(7, 3, sum))


# Using nested functions


from random import choice


# def colorize(thing):
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color
#
#     result = get_color() + ' ' + thing
#     return result
#
#
# print(colorize('apple'))

# Higher order functions, which return another function


# def make_color():
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color
#
#     return get_color
#
#
# first_color = make_color()
# print(first_color())
#
# second_color = make_color()
# print(second_color())
#
# third_color = make_color()
# print(third_color())


# Inner functions can access outer function scope


def colorize1(thing):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color + ' ' + thing

    return get_color


# print(colorize1('apple')())
colorized_dog = colorize1('dog')
print(colorized_dog())