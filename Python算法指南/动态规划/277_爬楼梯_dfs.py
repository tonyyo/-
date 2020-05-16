class Solution:
    def climbStairs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)

# 主函数
if __name__ == '__main__':
    n = 3
    print("爬的步数：", n)
    solution = Solution()
    string = ""
    result = []
    print(solution.climbStairs(n))
