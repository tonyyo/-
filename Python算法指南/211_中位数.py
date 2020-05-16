class Solution:
    def median(self, nums):
        nums.sort()
        return nums[(len(nums) - 1) // 2]
#主函数
if __name__ == "__main__":
    nums = [7, 9, 4, 5]
    #创建对象
    solution = Solution()
    print("输入的未排序的整数数组是：", nums)
    print("中位数是：", solution.median(nums))