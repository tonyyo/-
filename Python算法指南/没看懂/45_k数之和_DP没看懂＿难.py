class Solution:
    def kSum(self, A, k, target):
        n = len(A)
        dp = [
            [[0] * (target + 1) for _ in range(k + 1)],  # 三维列表, [0]也是一个列表
            [[0] * (target + 1) for _ in range(k + 1)],
        ]
        #dp[i][j][s]
        dp[0][0][0] = 1
        for i in range(1, n + 1):
            dp[i % 2][0][0] = 1
            for j in range(1, min(k + 1, i + 1)):    #前i个数里挑出j个数，和为s
                for s in range(1, target + 1):
                    dp[i % 2][j][s] = dp[(i - 1) % 2][j][s]  # 当前i - 1个数中就能找出j个数满足条件时
                    if s >= A[i - 1]: # 当前i - 1个数找不出k个数, 那就找一个加上最后一个数满足target的值
                        dp[i % 2][j][s] += dp[(i - 1) % 2][j - 1][s - A[i - 1]]
        return dp[n % 2][k][target]


# 主函数
if __name__ == '__main__':
    A = [1, 2, 3, 4]
    k = 2
    target = 5
    print("初始数组A：", A)
    print("整数k和目标值target：", k, target)
    solution = Solution()
    print("方案种类：", solution.kSum(A, k, target))