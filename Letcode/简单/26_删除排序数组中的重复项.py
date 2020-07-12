class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        left, right = 0, 0  # 定义快慢指针
        N = len(nums)
        while right < N:
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left + 1
if __name__ == '__main__':
    nums = [1, 1, 2]
    solution = Solution()
    print(solution.removeDuplicates(nums))
