class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, data):
        self.stack.append(data)
        val = min(data, self.min[-1]) if self.min else data
        self.min.append(val)

    def pop(self):
        self.stack.pop()
        if self.min:
            self.min.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min[-1]

