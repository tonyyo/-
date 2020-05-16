class Solution:
    def parseTernary(self, expression):
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
#主函数
if __name__ == "__main__":
    expression = "T?T?F:5:3"
    #创建对象
    solution = Solution()
    print("输入的表达式是：", expression)
    print("表达式的结果是：", solution.parseTernary(expression))