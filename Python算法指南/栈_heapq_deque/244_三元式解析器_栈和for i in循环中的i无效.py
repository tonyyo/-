class Solution:
    def parseTernary2(self, expression):
        objects = []
        i = len(expression) - 1
        while i >= 1:
            if expression[i] == '?':
                left, right = objects.pop(-1), objects.pop(-1)
                objects.append(left if expression[i - 1] == 'T' else right)
                i -= 1
            elif expression[i] != ':':
                objects.append(expression[i])
            i -= 1
        print(objects)
        return objects[0]

    def parseTernary1(self, expression):
        stack = []
        for i in range(len(expression) - 1, -1, -1):
            if expression[i] == '?':
                left, right = stack.pop(-1), stack.pop(-1)
                stack.append(left if expression[i - 1] == 'T' else right)
                i -= 1   # for in 循环中的i是局部变量, 在函数体里是无效的
            elif expression[i] != ':':
                stack.append(expression[i])
        print(stack)
        return stack[-1]

    def parseTernary(self, expression):
        stack = []
        i = len(expression) - 1
        while i >= 0:
            if expression[i] not in ['?', ':']:  # 遇到数字和T和F就加入栈
                stack.append(expression[i])
            if expression[i] == '?': # 遇到问号就要开始计算
                if len(stack) <= 1: # 防止出界
                    return stack[-1]
                temp1 = stack.pop()
                temp2 = stack.pop()
                if expression[i - 1] == 'T':
                    stack.append(temp1)
                if expression[i - 1] == 'F':
                    stack.append(temp2)
                i -= 1 # 因为遇到的是问号，所以需要多走一步
            i -= 1
        return stack


#主函数
if __name__ == "__main__":
    expression = "T?T?F:5:3"
    expression1 = "F?1:T?4:5"
    #创建对象
    solution = Solution()
    print("输入的表达式是：", expression)
    print("表达式的结果是：", solution.parseTernary(expression))
    print("表达式的结果是：", solution.parseTernary(expression1))