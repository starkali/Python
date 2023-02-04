# Higher other functions, which accept another functions as arguments

# def product(n, func):
#     result = 1
#     for number in range(1, n):
#         result *= func(number)
#     return result
#
# def square(x):
#     return x * x
#
# def cube(x):
#     return x * x * x
#
# print(product(4, square))
# print(product(4, cube))


# def my_function(a, b, func):
#     result = func([a, b])
#     return result

# print(my_function(7, 3, sum))

# Using nested functions

def colorize(thing):
    def get_clor():
        colors = ('red', 'green', 'yellow')
        color