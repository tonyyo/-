class Solution:
    def twoSum(self, n):
        ans = []
        f = [[0 for i in range(6 * n + 1)] for j in range(n + 1)]
        for i in range(1, 7):
            f[1][i] = 1.0 / 6.0  # 在python中其实除数为不为浮点数, 没有关系, 因为单个斜杠代表求浮点数商
        for i in range(2, n + 1):  # 从第二个骰子开始
            for j in range(i, 6 * n + 1):  # 多一个骰子多出六种情况
                for k in range(1, 7):
                    if j - k > 0:  # 当然不能为负数
                        f[i][j] += f[i - 1][j - k]
                f[i][j] /= 6  # 按理来说应该除以6*6, 但是前面每个阶段都除以了一个6, 所以这里只需要除以一个6
        for i in range(n, 6 * n + 1):
            ans.append(f[n][i])
        return ans
# 主函数
if __name__ == '__main__':
    n = 3
    solution = Solution()
    print("结果：", solution.twoSum(n))

