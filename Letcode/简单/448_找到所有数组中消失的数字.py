class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        N = len(nums)
        if N == 0:
            return []
        for i in range(N):
            index = abs(nums[i])
            nums[index - 1] = -abs(nums[index - 1]) # 数字比索引大1
        res = []
        for i in range(N):
            if nums[i] > 0:
                res.append(i + 1)
        return res