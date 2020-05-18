class Solution:
    def expressionExpand2(self, s):
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
                continue
            strs = []
            while stack and stack[-1] != '[':
                strs.append(stack.pop())
            # skip '['，跳过'['
            stack.pop()
            repeats = 0
            base = 1
            while stack and stack[-1].isdigit():
                repeats += (ord(stack.pop()) - ord('0')) * base
                base *= 10
            stack.append(''.join(reversed(strs)) * repeats)
        return ''.join(stack)

    def expressionExpand(self, s):
        left, right, num = 0, 0, 0
        while '[' in s:
            for i in range(len(s)):
                if s[i] == '[':
                    num = int(s[i - 1])
                    left = i
                if s[i] == ']':
                    right = i
                    break
            tempStr = ""
            for j in range(num):
                tempStr += s[left + 1 : right]
            s = s[:left - 1] + tempStr + s[right + 1:]
        return s



if __name__ == "__main__":
    expression = "4[ac]d2[dj]y"
    solution = Solution()
    print("输入的表达式是：", expression)
    print("展开的字符串是：", solution.expressionExpand(expression))
