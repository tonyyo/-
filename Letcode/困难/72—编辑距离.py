class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        dp = [[M+N for _ in range(N + 1)] for _ in range(M + 1)] # dp[i][j] 表示word1[:i]到word2[:j]的编辑距离
        for i in range(M + 1):
            for j in range(N + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    left = dp[i - 1][j] + 1
                    down = dp[i][j - 1] + 1
                    left_down = dp[i - 1][j - 1]
                    if word1[i - 1] != word2[j - 1]: # word1第i个字符和word2第j个字符相等时，相等的时候不需要替换操作
                        left_down += 1
                    dp[i][j] = min(left, down, left_down)
        return dp[M][N]

    def minDistance2(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)
        print(D)
        return D[n][m]
if __name__ == '__main__':
    solution = Solution()
    word1 = "horse"
    word2 = "ros"
    print(solution.minDistance(word1, word2))
    print(solution.minDistance2(word1, word2))