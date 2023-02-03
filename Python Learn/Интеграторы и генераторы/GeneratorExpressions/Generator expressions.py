def get_number_from_range():
    for number in range(10):
        yield number


counter = get_number_from_range()

print(counter)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

counter_1 = (number for number in range(10))
print(counter_1)
# print(next(counter_1))
# print(next(counter_1))
# print(next(counter_1))
# print(next(counter_1))
# print(next(counter_1))
# print(next(counter_1))
# print(next(counter_1))
# print(next(counter_1))


# print([number for number in range(10)])