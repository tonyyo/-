class Solution:
    def wiggleSort(self, nums):
        if not nums:
            return
        for i in range(1, len(nums)):
            should_swap = nums[i] < nums[i - 1] if i % 2 else nums[i] > nums[i - 1]
            if should_swap:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

    def wiggleSort2(self, nums):
        for i in range(1, len(nums)):
            if i % 2 == 1:
                if nums[i - 1] > nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
            else:
                if nums[i - 1] < nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
        return nums
#主函数
if __name__ == '__main__':
    nums = [3, 8, 7, 1, 6, 4]
    print("初始数组是：", nums)
    solution = Solution()
    solution.wiggleSort2(nums)
    print("结果是：", nums)