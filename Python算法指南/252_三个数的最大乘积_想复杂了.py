class Solution(object):
    def maximumProduct(self, nums):
        if not nums or len(nums) == 0:
            return 0
        nums.sort()
        res1 = nums[-1] * nums[-2] * nums[-3]
        res2 = nums[0] * nums[1] * nums[-1]
        return max(res1, res2)
#主函数
if __name__ == "__main__":
    nums = [1, 2, 3]
    #创建对象
    solution = Solution()
    print("输入的数组是 ：", nums)
    print("最大的积是:", solution.maximumProduct(nums))