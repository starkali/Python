# Map, Filter and Lambda Expressions

# map()

# def sum_of_two_numbers(x):
#     return x + x
#
#
# number_list = [1, 2, 3, 4, 5, 6, 7]
#
# result = map(sum_of_two_numbers, number_list)
# print(result)
#
# for item in result:
#     print(item)
#
# for item in map(sum_of_two_numbers, number_list):
#     print(item)
#
# print(list(map(sum_of_two_numbers, number_list)))

# def is_a_in_string(string):
#     if 'a' in string:
#         print('String has "a"')
#         return True
#     else:
#         print('String has not "a"')
#         return False
#
# string_list = ['hi', 'was', 'name', 'he']
#
# print(list(map(is_a_in_string, string_list)))

# filter()

# def is_number_odd(number):
#     return number % 2 == 1
#
#
# number_list = [1, 2, 3, 4, 5, 6, 7]
#
# print(filter(is_number_odd, number_list))
#
# print(list(filter(is_number_odd, number_list)))
#
# for number in filter(is_number_odd, number_list):
#     print(number)
#
# def is_a_in_string(string):
#     if 'a' in string:
#         print('String has "a"')
#         return True
#     else:
#         print('String has not "a"')
#         return False
#
# string_list = ['hi', 'was', 'name', 'he']
#
# print(list(filter(is_a_in_string, string_list)))


# Lambda Expression
# def cube(number):
#     return number ** 3




number_list = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda number: number ** 3, number_list)))
string_list = ['hi', 'was', 'name', 'he']
print(list(map(lambda string: string[-1], string_list)))
print(list(map(lambda string: string[::-1], string_list)))

print(list(filter(lambda number: number % 2 == 1, number_list)))
print(list(filter(lambda number: number % 2 == 0, number_list)))

