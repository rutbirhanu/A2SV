class MyQueue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop(-1)

    def peek(self) -> int:
        return self.stack1[-1]
    def size(self,stack):
        return len(stack)

    def empty(self) -> bool:
        return True if self.size(self.stack1)==0 else False

