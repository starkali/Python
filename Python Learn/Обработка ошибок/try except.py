# print('Some code')
# print(my_variable)
# print(len(23))
# try:
#     # print(my_variable)
#     print(len(23))
# except NameError:
#     print('NameError has happen')
# except TypeError:
#     print('TypeError has happen')
# print('Code after error')

user_dictionary = {'first_name': 'Jack', 'last_name': 'White', 'age': 24}

# print(user_dictionary['last_name'])
# print(user_dictionary['car'])

# print(user_dictionary.get('last_name'))
# print(user_dictionary.get('name'))

def get_dictionary_values(dictionary, key):
    '''
    If dictionary hasn't specified key, the function returns None
    :param dictionary:
    :param key:
    :return:
    '''
    try:
        return dictionary[key]
    except KeyError:
        return None


print(get_dictionary_values(user_dictionary, 'age'))
print(get_dictionary_values(user_dictionary, 'a'))
print(get_dictionary_values(user_dictionary, 'first_name'))


