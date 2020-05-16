#一个字符串数组
#该表达式的逆波兰表达式
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    def size(self):
        return len(self.items)
class Solution:
    def getLevel(self, s):
        if s == "+" or s == "-":
            return 1
        if s == "*" or s == "/":
            return 2
        return 0
    def convertToRPN(self, expression):
        RPN = []
        cal = Stack()
        for s in expression:
            if s == "(":
                cal.push(s)
            elif s == ")":
                while not cal.isEmpty() and cal.peek() != "(":
                    RPN.append(cal.peek())
                    cal.pop()
                cal.pop()  # 弹出左括号
            elif s.isdigit():
                RPN.append(s)
            else:
                if not cal.isEmpty():
                    if cal.peek() != "(":
                        while self.getLevel(cal.peek()) >= self.getLevel(s):
                            RPN.append(cal.peek())
                            cal.pop()
                            if cal.isEmpty():
                                break
                cal.push(s)
        while not cal.isEmpty():
            RPN.append(cal.peek())
            cal.pop()
        return RPN
#主函数
if __name__=="__main__":
     str=["3","-","4","+","5"]
     #创建对象
     solution=Solution()
     print("输入的表达式数组是：",str)
     print("表达式的逆波兰表达式是",solution.convertToRPN(str))