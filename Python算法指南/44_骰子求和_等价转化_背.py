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

# 主函数
if __name__ == '__main__':
    n = 2
    print("骰子的个数：", n)
    solution = Solution()
    print("结果：", solution.dicesSum(n))

# class Solution:
#     def dicesSum(self, n):
#         results = []
#         f = [[0 for j in range(6 * n + 1)] for i in range(n + 1)] # 列出所有可能出现的S值情况
#         for i in range(1, 7):  # 只有一个骰子时才有可能出现1-6的情况, 所以概率是固定的, 但这个不适合两个骰子的情况
#             f[1][i] = 1.0 / 6.0
#         for i in range(2, n + 1):    # 如果超过1个骰子
#             for j in range(i, 6 * n + 1): # 如果超过1个骰子, 可能出现的所有情况, 例如两个筛子的话, 可能的情况是2-12
#                 for k in range(1, 7):
#                     if j > k:
#                         f[i][j] += f[i - 1][j - k]  #解题思路:https://blog.csdn.net/aphysia/article/details/77855488
#                 f[i][j] /= 6.0
#         for i in range(n, 6 * n + 1):
#             results.append((i, f[n][i]))
#         return results
