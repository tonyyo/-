class Solution:
    def moveZeroes(self, nums):
        left, right = 0, 0  # left就是非0数的新位置。right往后找非0数的旧位置。
        while right < len(nums):
            if nums[right] != 0:  # 找到非0数旧位置，赋值给新位置
                nums[left] = nums[right]
                left += 1  # 新位置加1，等待接收下一个非0数旧位置
            right += 1

        while left < len(nums): # 省下的位置补0.
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
