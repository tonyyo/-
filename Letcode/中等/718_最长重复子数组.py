class Solution:
    def findLength(self, A: [int], B: [int]) -> int:
        M, N = len(A), len(B)
        maxLen = 0
        dp = [[0] * (N + 1) for _ in range(M + 1)]  # dp[i][j] 表示A以第i个字符结尾和B前j个字符结尾的最长重复子数组长度
        for i in range(M):
            for j in range(N):
                if A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                maxLen = max(maxLen, dp[i][j])
        return maxLen
if __name__ == '__main__':
    solution = Solution()
    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    print(solution.findLength(A, B))

