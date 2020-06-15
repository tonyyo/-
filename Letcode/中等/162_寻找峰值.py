class Solution:
    def findPeakElement(self, nums: [int]) -> int:
        N = len(nums)
        if N == 1:
            return  0
        if N == 2:
            return 1 if nums[1] > nums[0] else 0
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i
        return 0 if nums[0] > nums[1] else N - 1

    # def findPeakElement(self, nums: [int]) -> int:
    #     N = len(nums)
    #     left, right = 0, len(nums) - 1
    #     while left + 1 < right:
    #         mid = (left + right) // 2
    #         if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
    #             return nums[mid]
    #         elif nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
    #             start = mid
    #         else:
    #             end = mid
    #     if nums[left] > nums[right]:
    #         return left
    #     return end

