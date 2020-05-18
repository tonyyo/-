class Solution:
    def longestCommonSubsequence2(self, A, B):
        n, m = len(A), len(B)
        f = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(n):
            for j in range(m):
                f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
                if A[i] == B[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
        return f[n][m]

    def longestCommonSubsequence(self, A, B):
        lenA = len(A)
        lenB = len(B)
        f = [[0] * (lenB + 1) for _ in range(lenA + 1)]  # f[i][j]表示i长度的A和j长度的B的最长公共子序列
        for i in range(lenA):
            for j in range(lenB):
                f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
                if A[i] == B[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
        return f[lenA][lenB]
#主函数
if __name__ == '__main__':
    A = "ABCDB"
    B = "EACDB"
    print("序列A：", A)
    print("序列B：", B)
    solution = Solution()
    print("最长公共子序列长度：", solution.longestCommonSubsequence(A, B))