def vowel_filter(function):
    def wrapper():
        return [letter for letter in function() if letter in "aoeyiu"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
