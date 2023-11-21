class sequence_repeat:
    def __init__(self, sequence, number: int):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration
        result = self.sequence[self.index]
        self.index = (self.index + 1) % len(self.sequence)
        self.number -= 1
        return result


# Test Case 1
result1 = sequence_repeat('abc', 5)
for item in result1:
    print(item, end='')

# Test Case 2
result2 = sequence_repeat('I Love Python', 3)
for item in result2:
    print(item, end='')
