class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if not self.stack1:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        val = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return val