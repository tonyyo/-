class Solution:
    def findPeakElement(self, nums: [int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]: # left指向右侧更大的元素
                left = mid + 1
            else:                         # right指向左侧更大的原则
                right = mid
        return right            # 所以当left==right时，双指针所指元素就是峰值

