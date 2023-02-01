import shelve

with shelve.open('shelve_test') as cars:
    cars['l'] = 'Germany'
    cars['ford'] = 'USA'
    cars['mazda'] = 'Japan'
    cars['renault'] = 'France'

    print(cars['ford'])
    print(cars['renault'])
    print(cars['opel'])

# print(cars['mazda']) # error

    del cars['opel']

    for key in cars:
        print(key)