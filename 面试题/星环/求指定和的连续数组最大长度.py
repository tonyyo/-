class Solution:
   def findMaxLen(self, nums, target):
        N, MaxLen = len(nums), 0
        dp, prefixSum = [0] *N, [0] * N
        for i in range(N):
            if i == 0:
                prefixSum[i] = nums[i]
            else:
                prefixSum[i] = prefixSum[i - 1] + nums[i]
            for j in range(i):
                if prefixSum[i] - prefixSum[j] == target:
                    MaxLen = max(MaxLen, i - j)
        return MaxLen

if __name__ == '__main__':
    s = Solution()
    print(s.findMaxLen([1, -1, 1, 0, -1, 2], 1))






