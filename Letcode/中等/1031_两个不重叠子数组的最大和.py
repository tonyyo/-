class Solution:
    def maxSumTwoNoOverlap(self, A: [int], L: int, M: int) -> int:
        N = len(A)
        preSum = [0] * (N + 1)  # 前n项和
        for i in range(1, N + 1):
            preSum[i] = preSum[i - 1] + A[i - 1]
        LM = self.sumOfTwoArr(preSum, L, M)
        ML = self.sumOfTwoArr(preSum, M, L)
        return max(LM, ML)

    def sumOfTwoArr(self, preSum, L, M):
        N = len(preSum)
        Lmax, Max = [0] * N, [0] * N # Lmax[i]前i项长度为L的最大子数组和
        for i in range(L, N):
            Lmax[i] = max(Lmax[i - 1], preSum[i] - preSum[i - L])
        for j in range(L + M, N):
            Max[j] = max(Max[j - 1], Lmax[j] + preSum[j] - preSum[j - M])  # 不能单独计算Rmax
        print(Lmax)
        print(Max)
        return Max[-1]
if __name__ == '__main__':
    solution = Solution()
    A = [0,6,5,2,2,5,1,9,4]
    L, M = 1, 2
    print(solution.maxSumTwoNoOverlap(A, L, M))