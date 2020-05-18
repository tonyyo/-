class Solution(object):
    def isValidParentheses(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')':
                if stack.pop() != '(':
                    return False
            elif s[i] == ']':
                if stack.pop() != '[':
                    return False
            else:
                if stack.pop() != '{':
                    return False
        return True if len(stack) == 0 else False

#主函数
if  __name__=="__main__":
    s="()[{}]"
    #创建对象
    solution=Solution()
    print("输入的包含括号的字符串是：",s)
    print("输出的结果是：", solution.isValidParentheses(s))