rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue',
                  'indigo', 'violet'}
print(rainbow_colors)
print(type(rainbow_colors))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 43, 56, 3, 3, 3, 3]
text_tuple = ('sfds', 'aafg', 'afadsf', 'hi', 'hi', 'hi')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(777)
set_from_tuple.add('hello')
set_from_list.add(777)
set_from_tuple.add('hello')

x = set_from_list.pop()
set_from_list.remove(3)
set_from_list.discard(43)
# set_from_list.remove(3)
set_from_list.discard(3)
set_from_list.clear()

print(set_from_list)
print(set_from_tuple)
print(x)