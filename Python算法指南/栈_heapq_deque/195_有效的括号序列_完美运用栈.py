class Solution(object):
    def isValid(self, s):
        stack = []
        if len(s) == 1:
            return False
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif stack and s[i] == ')':
                if stack.pop() != '(':
                    return False
            elif stack and s[i] == ']':
                if stack.pop() != '[':
                    return False
            elif stack and s[i] == '}':
                if stack.pop() != '{':
                    return False
        return True if len(stack) == 0 else False

#主函数
if  __name__=="__main__":
    s="()]"
    #创建对象
    solution=Solution()
    print("输入的包含括号的字符串是：",s)
    print("输出的结果是：", solution.isValid(s))