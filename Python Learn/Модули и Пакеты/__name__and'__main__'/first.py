def function_1():
    print('funciton_1() from first.py')

print('Top level in first.py')

if __name__ == '__main__':
    print('first.py is being run directly')
else:
    print('first.py has been imported')