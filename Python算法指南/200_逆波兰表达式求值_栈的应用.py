class Solution:
    def evalRPN2(self, tokens):
        stack = []
        for i in tokens:
            if i not in ('+', '-', '*', '/'): # 数字入栈
                stack.append(int(i))
            else:
                op2 = stack.pop()   # 先出栈的是第二个操作数
                op1 = stack.pop()   # 后出栈的是第一个操作数
                if i == '+': stack.append(op1 + op2)
                elif i == '-': stack.append(op1 - op2)
                elif i == '*': stack.append(op1 * op2)
                else: stack.append(int(op1 / op2))  # 题目规定取整
        return stack[0]
#主函数
if  __name__=="__main__":
    tokens=["2", "1", "+", "3", "*"]
    #创建对象
    solution=Solution()
    print("输入的逆波兰表达式是：",tokens)
    print("计算逆波兰表达式的结果是：", solution.evalRPN(tokens))