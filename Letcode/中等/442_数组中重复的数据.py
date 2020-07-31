class Solution:
    def findDuplicates(self, nums: [int]) -> [int]:
        N, res = len(nums), []
        for num in nums:
            index = abs(num) - 1 # 因为nums里的值是1-n
            if nums[index] < 0:
                res.append(index + 1)
            nums[index] = -abs(nums[index]) # 防止负负得正
        return res