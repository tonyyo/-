class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        nums.sort()
        return self.nSum(nums, target, 4)

    def nSum(self, nums, target, n):
        if n == 2:
            return self.twoSum(nums, target)
        else:
            res = []
            for i in range(len(nums) - n + 1): # 留出后续n个数的位置
                temp = self.nSum(nums[i + 1:], target - nums[i], n - 1)
                for x in temp:
                    res.append([nums[i]] + x)
            return res

    def twoSum(self, nums, target): # 返回两数之和等于target的组合，所以不能用hash表，因为要去重
        N, res = len(nums), []
        left, right = 0, N - 1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                while left + 1 < N and nums[left] == nums[left + 1]: # 因此nums需要时排序的，方便去重
                    left += 1
                while right - 1 >= 0 and nums[right - 1] == nums[right]:
                    right -= 1
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
        return res