class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(n - 2):
            temp = b
            b = a + b
            a = temp
        return b
if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(5))
