from functools import wraps

def prohibit_kwargs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('Keyword arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper

def prohibit_kwargs_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for val in args:
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
        for key, val in kwargs.items():
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
            return func(*args, **kwargs)
        if kwargs:
            raise ValueError('Keyword arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper

@prohibit_kwargs
def print_hello(name):
    print(f'Hello {name}!')

print_hello('Jack')
print_hello(3)