class Solution:
    def findLength(self, A: [int], B: [int]) -> int:
        M, N = len(A), len(B)
        maxLen = 0
        dp = [[0] * N for _ in range(M)]  # dp[i][j] 表示A以A[i]结尾和B以B[j]结尾的最长重复子数组长度
        for i in range(M):
            for j in range(N):
                if A[i] == B[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
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

