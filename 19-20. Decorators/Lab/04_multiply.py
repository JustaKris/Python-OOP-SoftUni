def multiply(times: int):
    def decorator(funtion):
        def wrapper(*args, **kwargs):
            result = funtion(*args, **kwargs)
            return result * times
        return wrapper
    return decorator


# Test case 1
@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))


# Test case 2
@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
