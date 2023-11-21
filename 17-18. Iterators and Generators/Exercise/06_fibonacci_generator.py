def fibonacci():
    current, next_value = 0, 1
    while True:
        yield current
        current, next_value = next_value, current + next_value


# Test case 1
generator = fibonacci()
for i in range(5):
    print(next(generator))

# Test case 2
generator = fibonacci()
for i in range(1):
    print(next(generator))
