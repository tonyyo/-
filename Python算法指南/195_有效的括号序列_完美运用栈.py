class Solution(object):
    def isValid(self, s):
        length = len(s)
        stack = []
        for i in range(length):
            if s[i] == '(' or s[i] == '[' or s[i] == '{': # 左括号进栈
                stack.append(s[i])
            else:
                if len(stack) == 0:  # 防止stack[-1]溢栈
                    return False
                elif s[i] == ')' and stack[-1] != '(' or s[i] == ']' and stack[-1] != '[' or s[i] == '}' and stack[-1] != '{':
                    return False
                else:       # 遇到右括号时，弹栈的那个括号必须是对应的左括号
                    stack.pop()
        return True if len(stack) == 0 else False  # 排除只有左括号的情况


#主函数
if  __name__=="__main__":
    s="}{"
    #创建对象
    solution=Solution()
    print("输入的包含括号的字符串是：",s)
    print("输出的结果是：", solution.isValid(s))