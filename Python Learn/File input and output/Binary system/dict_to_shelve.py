import shelve

university = shelve.open('university_file')
# university['schedules'] = {
#
#         'monday_schedule': ['Math', 'English language', 'System programming', 'Python'],
#         'tuesday_schedule': ['English language', 'HTML', 'Python', 'Football'],
#         'wednesday_schedule': ['Physics', 'English language', 'Python'],
#         'thursday_schedule': ['Math', 'Chemistry', 'Java'],
#         'friday_schedule': ['Running', 'Math', 'Python']
#     }
# university['tutors'] = {
#         'Math': ['Jack White', 'Jim Black'],
#         'Python': ['YouRa Allakhverdov', 'Jane Smith']
#     }

# x = university['schedules']
# print(type(x))
print(university['schedules']['wednesday_schedule'])
print(university['tutors']['Math'])

university.close()

# university = {
#     'schedules': {
#         'monday_schedule': ['Math', 'English language', 'System programming', 'Python'],
#         'tuesday_schedule': ['English language', 'HTML', 'Python', 'Football'],
#         'wednesday_schedule': ['Physics', 'English language', 'Python'],
#         'thursday_schedule': ['Math', 'Chemistry', 'Java'],
#         'friday_schedule': ['Running', 'Math', 'Python']
#     },
#
#     'tutors': {
#         'Math': ['Jack White', 'Jim Black'],
#         'Python': ['YouRa Allakhverdov', 'Jane Smith']
#     }
# }
#
# print(university['schedules']['wednesday_schedule'])
# print(university['tutors']['Math'])

