# # built-in functions
# x = print('Hello!')
# y = set()
#
# print(type(x))
# print(type(y))
#
# print(x)
# print(y)
#
# # built-in methods
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)
# my_list.clear()
# print(my_list)

# def print_greeting():
#     '''
#     Print 'Hello!' text
#     :return: None
#     '''
#     print('Hello!')
#
# # call the function
# print_greeting()
#
# # receive the description of the function
# help(print_greeting)

# def print_greeting_with_name(name = 'Name'):
#     '''
#     :param name
#     :return: None
#     '''
#     print('Hello ' + name + '!')
# print_greeting_with_name('Jack')
# help(print_greeting_with_name)
# print_greeting_with_name()
# x = print_greeting_with_name('Jane')
# print(x)

# def sum_of_two_numbers(a = 0, b = 0):
#     '''
#
#     :param a: The first addend
#     :param b: The second addend
#     :return: Sum of a and b
#     '''
#     return a + b
# x = sum_of_two_numbers(45, 7)
# x = sum_of_two_numbers()
# print(x)
# help(sum_of_two_numbers)

# def is_hello_in_text(text):
#     if 'hello' in text.lower():
#         return True
#     else:
#         return False
# print(is_hello_in_text('Hello everyone!'))

# def is_hello_in_text(text):
#     return 'hello' in text.lower()
#
# print(is_hello_in_text('everyone!'))
#
# def is_string_in_text(string, text):
#     return string in text
# print(is_string_in_text('he', 'The apple'))
# print(is_string_in_text('hey', 'The apple'))

# def greeting_depends_on_gender(name, gender):
#     if gender == 'male':
#         print('Hello ' + name + '! You look great!')
#         return gender
#     elif gender == 'female':
#         print('Hello ' + name + '! You are so nice!')
#         return gender
#     else:
#         print('Hello ' + name + '! I\'ve never seen the creature like you!')
#         return gender
#
#
# returned_value = greeting_depends_on_gender('Jack', 'male')
# returned_value = greeting_depends_on_gender('Jane', 'female')
# returned_value = greeting_depends_on_gender('Ja', 'cmale')

def greeting_depends_on_gender(name, gender):
    if gender == 'male':
        return gender
        print('Hello ' + name + '! You look great!')
    elif gender == 'female':
        print('Hello ' + name + '! You are so nice!')
        return gender
    else:
        print('Hello ' + name + '! I\'ve never seen the creature like you!')
        return gender


returned_value_1 = greeting_depends_on_gender('Jack', 'male')
returned_value_2 = greeting_depends_on_gender('Jane', 'female')
returned_value_3 = greeting_depends_on_gender('Ja', 'cmale')

print(returned_value_1)
print(returned_value_2)
print(returned_value_3)
