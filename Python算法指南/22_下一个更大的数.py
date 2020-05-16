class Solution:
    def nextGreaterElements(self, nums):
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if i == len(nums) - 1:
                ans[i] = 2
                break
            ans[i] = nums[i + 1] if nums[i] < nums[i + 1] and i + 1 < len(nums) else -1
        return ans

if __name__ == '__main__':
    nums = [1, 2, 1]
    solution = Solution()
    print(solution.nextGreaterElements(nums))