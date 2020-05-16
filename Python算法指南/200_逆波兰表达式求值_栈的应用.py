class Solution:
    def evalRPN2(self, tokens):
        stack = []
        for i in tokens:
            if i not in ('+', '-', '*', '/'):
                stack.append(int(i))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if i == '+': stack.append(op1 + op2)
                elif i == '-': stack.append(op1 - op2)
                elif i == '*': stack.append(op1 * op2)
                else: stack.append(int(op1 * 1.0 / op2))
        return stack[0]

    def evalRPN(self, tokens):
        size = len(tokens)
        stack = []
        for x in tokens:
            if x not in ["+", "-", "*", "/"]:
                stack.append(x)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                result = 0
                if x == "+":
                    result = a + b
                if x == "-":
                    result = a - b
                if x == "*":
                    result = a * b
                if x == "/":
                    result = a / b
                stack.append(result)
        return stack[-1]

#主函数
if  __name__=="__main__":
    tokens=["2", "1", "+", "3", "*"]
    #创建对象
    solution=Solution()
    print("输入的逆波兰表达式是：",tokens)
    print("计算逆波兰表达式的结果是：", solution.evalRPN(tokens))