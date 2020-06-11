class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        N = len(nums)
        if N == 0:
            return [-1, -1]
        left1, left2, right1, right2 = 0, 0, N - 1, N - 1
        while left1 < right1:
            mid = (left1 + right1) // 2
            if target > nums[mid]:
                left1 = mid + 1
            else:
                right1 = mid

        while left2 < right2:
            mid2 = (left2 + right2) // 2 + 1
            if target < nums[mid2]:
                right2 = mid2 - 1
            else:
                left2 = mid2

        if nums[left1] == target and nums[left2] == target:
            return [left1, left2]
        else:
            return [-1, -1]

if __name__ == '__main__':
    solution = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print(solution.searchRange(nums, target))
