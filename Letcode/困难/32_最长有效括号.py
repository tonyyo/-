class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, maxLen, N = [], 0, len(s)
        stack.append(-1) # 赋值一个-1的坐标
        for i in range(N):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                stack.pop()
                if not stack:  # 表明-1被弹出了，需要加一个新的-1
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i - stack[-1])
        return maxLen
