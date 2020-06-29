class Solution:
    def sortArrayByParity(self, nums):
        start, end = 0, len(nums) - 1
        while start < end:
            while start < end and nums[start] % 2 == 0: # 找到奇数为止
                start += 1
            while start < end and nums[end] % 2 == 1:  # 找到偶数为止
                end -= 1
            if start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return nums

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solution = Solution()
    print("输入的数组是：", nums)
    print("奇偶分割数组后的结果是：", solution.partitionArray2(nums))
