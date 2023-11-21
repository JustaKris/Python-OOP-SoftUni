class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dict_tuple = tuple(dictionary.items())  # returns list of tuples for each key-value pair in dictionary
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.dict_tuple):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.dict_tuple[index]


# Test 1
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

# Test 2
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
