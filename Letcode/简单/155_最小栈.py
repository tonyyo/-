class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        tempStack = []
        while self.minStack and self.minStack[-1] < x: # 新加入的元素比栈顶大
            tempStack.append(self.minStack.pop())
        self.minStack.append(x)
        while tempStack:
            self.minStack.append(tempStack.pop())

    def pop(self) -> None:
        top = self.stack.pop()
        tempStack = []
        while self.minStack and self.minStack[-1] != top:
            tempStack.append(self.minStack.pop())
        self.minStack.pop()
        while tempStack:
            self.minStack.append(tempStack.pop())

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]