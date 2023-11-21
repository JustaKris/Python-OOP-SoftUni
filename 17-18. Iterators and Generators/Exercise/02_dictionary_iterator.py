class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.dictionary):
            raise StopIteration
        else:
            result = [(key, value) for key, value in self.dictionary.items()][self.index]
            self.index += 1
            return result


# Test 1
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

# Test 2
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
