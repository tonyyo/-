class Solution:
    def climbStairs1(self, n):
        if n == 0:
            return 1
        if n <= 2:
            return n
        result = [1, 2]
        for i in range(n - 2):
            result.append(result[-2] + result[-1])
        return result[-1]

    def climbStairs(self, n, string, result):
        if n == 0:
            result.append(string)
            return
        if n < 0:
            return
        for i in range(1, 3):
            self.climbStairs(n - i, string + str(i), result)

# 主函数
if __name__ == '__main__':
    n = 3
    print("爬的步数：", n)
    solution = Solution()
    string = ""
    result = []
    solution.climbStairs(n, string, result)
    print(result)
    print(len(result))
