class Solution:
    def dicesSum(self, n):
        ans = []
        f = [[0 for i in range(6 * n + 1)] for j in range(n + 1)]
        for i in range(1, 7):
            f[1][i] = 1.0 / 6.0  # 在python中其实除数为不为浮点数, 没有关系, 因为有两个除号
        for i in range(2, n + 1):
            for j in range(n, 6 * n + 1):
                for k in range(1, 7):
                    if j > k:  # 当然不能为负数
                        f[i][j] += f[i - 1][j - k]
                f[i][j] /= 6  # 按理来说应该除以6*6, 但是前面每个阶段都除以了一个6, 所以这里只需要除以一个6
        for i in range(n, 6 * n + 1):
            ans.append(f[n][i])
        return ans

    def dicesSum2(self, n):
        List = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]  # 横竖都多一行， 对应6 * n种情况，
        for i in range(1, 7):
            List[1][i] = 1 / 6
        for i in range(2, n + 1):  # 2 - n个骰子的行
            for j in range(i, 6 * i + 1):  # n个骰子最小数就是n
                for k in range(1, 7):
                    if j > k:
                        List[i][j] += List[i - 1][j - k]  # 找到能够组成该值的所有可能概率前部
                List[i][j] /= 6  # 找到该值可能概率的后部
        result = []
        for x in List[n]:
            if x != 0: # 去0
                result.append(x)
        return result

# 主函数
if __name__ == '__main__':
    n = 2
    solution = Solution()
    print("结果：", solution.dicesSum(n))
    print("结果：", solution.dicesSum2(n))

