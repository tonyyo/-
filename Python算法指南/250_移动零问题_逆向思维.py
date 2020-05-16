class Solution:
    def moveZeroes1(self, nums):
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                if left != right:
                    nums[left] = nums[right]
                left += 1
            right += 1
        while left < len(nums):
            if nums[left] != 0:
                nums[left] = 0
            left += 1
        return nums

    def moveZeroes(self, nums):
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
                right += 1
            else:
                right += 1
        while left < len(nums):
            nums[left] = 0
            left += 1
        return nums


# 主函数
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    # 创建对象
    solution = Solution()
    print("输入的整数数组是 ：", nums)
    nums = solution.moveZeroes(nums)
    print("移动零后的数组是:", nums)
