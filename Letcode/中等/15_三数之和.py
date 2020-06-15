class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums = sorted(nums)
        N = len(nums)
        res = []
        start = 0
        while start < N:
            first = nums[start]
            if first > 0:   # 因为已拍好序，第一个大于0， 那么不可能再等于0
                return res
            nextSum = 0 - first
            left, right = start + 1, N - 1
            while left < right:
                if left == start:
                    left += 1
                elif right == start:
                    right -= 1
                else:
                    if nums[left] + nums[right] == nextSum:
                        temp = [nums[start], nums[left], nums[right]]
                        while start + 1 < N and nums[start] == nums[start + 1]:
                            start += 1
                        while left + 1 < N and nums[left] == nums[left + 1]:  # 去重
                            left += 1
                        while right + 1 < N and nums[right] == nums[right - 1]:
                            right -= 1
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
    print(solution.threeSum([0,0,0]))
