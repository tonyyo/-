class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push1(self, number):
        self.stack.append(number)
        if not self.min_stack or number <= self.min_stack[-1]:
            self.min_stack.append(number)
    def pop1(self):
        number = self.stack.pop()
        if number == self.min_stack[-1]:
            self.min_stack.pop()
        return number
    def min1(self):
        return self.min_stack[-1]

#主函数
if  __name__=="__main__":
     minZ=MinStack()
     list=[]
     minZ.push(1)
     list.append(minZ.pop())
     minZ.push(2)
     minZ.push(3)
     list.append(minZ.min())
     minZ.push(1)
     list.append(minZ.min())
     print("输入的顺序是：push(1),pop(),push(2),push(3),min(),push(1),min()")
     print("输出的结果是：",list)