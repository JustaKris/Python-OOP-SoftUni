def solution():
    def integers():
        current = 1
        while True:
            yield current
            current += 1

    def halves():
        for num in integers():
            yield num / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return take, halves, integers


# Test Case 1
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

# Test Case 2
take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
