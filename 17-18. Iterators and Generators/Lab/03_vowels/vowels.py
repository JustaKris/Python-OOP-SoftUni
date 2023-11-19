class vowels:
    def __init__(self, text: str):
        self.vowels_found = [char for char in text if char.lower() in 'aieuyo']
        self.current_index = 0
        self.end_index = len(self.vowels_found) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > self.end_index:
            raise StopIteration()
        index = self.current_index
        self.current_index += 1
        return self.vowels_found[index]
