class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        N, hash, maxLen = len(nums), set(), 0
        for i in range(N):
            hash.add(nums[i])
        for i in range(N):
            if nums[i] - 1 in hash:
                continue
            currentLen, currentVal = 1, nums[i] + 1
            while currentVal in hash:
                currentLen += 1
                currentVal += 1
            maxLen = max(maxLen, currentLen)
        return maxLen

