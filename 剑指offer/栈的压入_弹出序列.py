class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = [] # 辅助栈
        while pushV:
            if pushV[0] != popV[0]:  # 不相等，入辅助栈
                stack.append(pushV.pop(0))
            else:                    # 相等，跳过
                pushV.pop(0)
                popV.pop(0)
        if popV and stack and popV == stack[::-1]:   # 比较辅助栈和省下的popV是否相等
            return True
        elif not popV and not stack:    # 没有利用到辅助栈， 返回True
            return  True
        else:
            return False


if __name__ == '__main__':
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    solution = Solution()
    print((solution.IsPopOrder(pushV, popV)))
