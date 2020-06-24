class Solution():
    def jump(self, line):
        N = len(line)
        # dp = [0] * N  # dp[i] 表示跳到第i格获取的最高积分
        # dp[0] = 0
        pre, cur = 0, 0
        for i in range(N):
            # dp[i] = max(dp[i - 1], dp[i - 2] + line[i])
            pre, cur = cur, max(cur, pre + line[i])
        # print(line)
        # print(dp)
        print(cur)

if __name__ == '__main__':
    solution = Solution()
    N = int(input())
    line = list(map(int, input().strip().split()))  # 单行将一行数字存入列表
    solution.jump(line)

