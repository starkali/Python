# car_prices = {'opel': 5000, 'toyota': 7000, 'bmw': 10000 }
# print(car_prices)
# print(car_prices['toyota'])
# car_prices['mazda'] = 4000
# print(car_prices)
# car_prices['opel'] = 2000
# print(car_prices)
# del car_prices['toyota']
# print(car_prices)
# # del car_prices
# car_prices.clear()
# print(car_prices)

person = {
    'first name': 'Jack',
    'last name': 'Brown',
    'age': 43,
    'hobbies': ['football', 'singing', 'photo'],
    'children': {'son': 'Michael', 'daugter': 'Pamela'}
}

print(person['age'])
print(person['hobbies'])
hobbies = person['hobbies']
print(hobbies[2])

print(person['hobbies'][2])


children = person['children']
print(children['son'])

print(person['children']['son'])

person['car'] = 'Mazda'
person['hobbies'][0] = 'basketball'

print(person.keys())
print(person.values())
print(person.items())