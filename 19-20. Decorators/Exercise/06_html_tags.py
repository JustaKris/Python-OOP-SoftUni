def tags(tag):
    def decorator(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"
        return wrapper
    return decorator


# Test case 1
@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


# Test case 2
@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
