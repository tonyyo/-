class Solution(object):
    def isValidParentheses2(self, s):
        stack = []
        for ch in s:
            #压栈
            if ch == '{' or ch == '[' or ch == '(':
                stack.append(ch)
            else:
                #栈需非空
                if not stack:
                    return False
                #判断栈顶是否匹配
                if ch == ']' and stack[-1] != '[' or ch == ')' and stack[-1] != '(' or ch == '}' and stack[-1] != '{':
                    return False
                #弹栈
                stack.pop()
        return not stack

    def isValidParentheses(self, s):
        length = len(s)
        stack = []
        for i in range(length):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if s[i] == ')' and stack[-1] != '(' or s[i] == ']' and stack[-1] != '[' or s[i] == '}' and stack[-1] != '{':
                    return False
                else:
                    stack.pop()
        return True


#主函数
if  __name__=="__main__":
    s="()[{}]"
    #创建对象
    solution=Solution()
    print("输入的包含括号的字符串是：",s)
    print("输出的结果是：", solution.isValidParentheses(s))