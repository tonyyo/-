class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums = sorted(nums)
        N = len(nums)
        res = []
        start = 0
        while start < N:
            first = nums[start]
            if first > 0:   # 因为已排好序，第一个大于0， 那么不可能再等于0
                return res
            nextSum = 0 - first
            left, right = start + 1, N - 1
            while left < right:
                if nums[left] + nums[right] == nextSum:
                    while start + 1 < N and nums[start] == nums[start + 1]:  # 去重
                        start += 1
                    while left + 1 < N and nums[left] == nums[left + 1]:  # 去重
                        left += 1
                    while right + 1 < N and nums[right] == nums[right - 1]:
                        right -= 1
                    temp = [nums[start], nums[left], nums[right]]
                    res.append(temp[:])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < nextSum:
                    left += 1
                else:
                    right -= 1
            start += 1
        return res
if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
