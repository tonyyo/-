class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def adjust(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
    def push(self, element):
        self.stack1.append(element)
    def top(self):
        self.adjust()
        return self.stack2[- 1]
    def pop(self):
        self.adjust()           # 栈1不能实现，要栈2辅助
        return self.stack2.pop() # 实现先进先出
#主函数
if __name__ == "__main__":
    solution = Solution()
    list1 = []
    solution.push(1)
    list1.append(solution.pop())
    solution.push(2)
    solution.push(3)
    list1.append(solution.top())
    list1.append(solution.pop())
    print("输入的顺序为：push(1),pop(),push(2),push(3),top(),pop()")
    print("输出的结果为：", list1)