class countdown_iterator:
    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 0:
            raise StopIteration
        else:
            result = self.count
            self.count -= 1
            return result


# Test 1
iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

# Test 2
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
