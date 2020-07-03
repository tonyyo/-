class Solution:
    def validateStackSequences(self, pushed: [int], popped: [int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num) # num 入栈
            while stack and stack[-1] == popped[i]: # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack

if __name__ == '__main__':
    solution = Solution()
    pushed = [2,1,0]
    popped = [1,2,0]
    print(solution.validateStackSequences(pushed, popped))