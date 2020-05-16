import sys
class Solution:
    def MinAdjustmentCost1(self, A, target):
        f = [[sys.maxsize for j in range(101)] for i in range(len(A) + 1)]
        for i in range(101):
            f[0][i] = 0
        n = len(A)
        for i in range(1, n + 1):
            for j in range(101):
                if f[i - 1][j] != sys.maxsize:
                    for k in range(101):
                        if abs(j - k) <= target:
                            f[i][k] = min(f[i][k], f[i - 1][j] + abs(A[i - 1] - k))
        ans = f[n][100]
        print(f)
        for i in range(101):
            if f[n][i] < ans:
                ans = f[n][i]
        return ans

    # def MinAdjustmentCost(self, A, target):
    #     f = [[65536] * max(A) for _ in range(len(A) + 1)]
    #     for i in range(1, len(A) + 1):


# 主函数
if __name__ == '__main__':
    A = [1, 4, 2, 3]
    target = 1
    print("初始数组：", A)
    print("相邻两个数的最大值：", target)
    solution = Solution()
    print("最小调整代价：", solution.MinAdjustmentCost(A, target))
