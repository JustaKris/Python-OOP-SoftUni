class Stack:
    def __init__(self):
        self.data: list = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        # return len(self.data) == 0
        return any(self.data)

    def __str__(self):
        return f"[{', '.join([str(el) for el in reversed(self.data)])}]"


stack = Stack()
stack.push(3)
stack.push(7)
stack.push(12)

print(stack)
