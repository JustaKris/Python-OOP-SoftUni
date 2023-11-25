def logged(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"you called {func.__name__}{args}\nit returned {result}"
    return wrapper


# Test case 1
@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


# Test case 2
@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
