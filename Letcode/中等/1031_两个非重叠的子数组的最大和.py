import copy


class Solution:
    def maxSumTwoNoOverlap(self, A: [int], L: int, M: int) -> int:
        N = len(A)
        prefixSum = copy.deepcopy(A)
        for i in range(1, N):
            prefixSum[i] += prefixSum[i - 1] # 求前缀和
        return max(self.maxSum(prefixSum, L, M), self.maxSum(prefixSum, M, L))

    def maxSum(self, prefixSum, len1, len2):
        N = len(prefixSum)
        sumL = copy.deepcopy(prefixSum)  # sumL[i]表示到i位置,长度为L的最大子数组和
        dp = copy.deepcopy(prefixSum)    # dp[i]表示到i位置，两子数组的最大和
        for i in range(len1, N):
            sumL[i] = max(sumL[i - 1], prefixSum[i] - prefixSum[i - len1])
        for i in range(len1 + len2, N):
            dp[i] = max(dp[i - 1], sumL[i - len2] + prefixSum[i] - prefixSum[i - len2])
        return dp[-1]


    def maxSumTwoNoOverlap1(self, A: [int], L: int, M: int) -> int:
        N, leftLSum, leftRSum, rightLsum, rightMsum, totalSum = len(A), 0, 0, 0, 0, 0
        for i in range(N + 1):
            leftLSum = self.maxSumOfLen(A[:i], L) if L <= i else 0
            leftRSum = self.maxSumOfLen(A[:i], M) if M <= i else 0
            rightLsum = self.maxSumOfLen(A[i:], L) if L <= N - i else 0
            rightMsum = self.maxSumOfLen(A[i:], M) if M <= N - i else 0
            totalSum = max(totalSum, leftLSum + rightMsum, rightLsum + leftRSum)
        return  totalSum

    def maxSumOfLen1(self, arr, length):
        maxSum = 0
        N = len(arr)
        for i in range(N - length + 1):
            subArr = arr[i : i + length]
            maxSum = max(maxSum, sum(subArr))
        return maxSum

if __name__ == '__main__':
    solution = Solution()
    A = [0,6,5,2,2,5,1,9,4]
    print(solution.maxSumTwoNoOverlap(A, 1, 2))