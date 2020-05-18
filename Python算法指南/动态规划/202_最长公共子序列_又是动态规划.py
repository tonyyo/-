class Solution:
    def longestCommonSubsequence(self, A, B):
        n, m = len(A), len(B)
        f = [[0] * (n + 1) for i in range(m + 1)] # f[i][j]存的是A中前i个元素和B中前j个元素的最长公共子序列长度
        for i in range(n):
            for j in range(m):
                if A[i] != B[j]:
                    f[i][j] = max(f[i][j - 1], f[i - 1][j]) # 如果不相等，那么肯定等于上一行或上一列中的最大值
                else:
                    f[i][j] = f[i - 1][j - 1] + 1 # 如果相等，那么二者的字符串长度同时加1，公共长度也加1
        print(f)
        return f[n - 1][m - 1]

#主函数
if __name__ == '__main__':
    A = "ABCDB"
    B = "EACDB"
    print("序列A：", A)
    print("序列B：", B)
    solution = Solution()
    print("最长公共子序列长度：", solution.longestCommonSubsequence(A, B))