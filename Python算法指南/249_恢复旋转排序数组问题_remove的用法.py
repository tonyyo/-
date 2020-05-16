class Solution:
    def recoverRotatedSortedArray(self, nums):
        pos = nums.index(min(nums))
        i = 0
        while i < pos:
            nums.append(nums[0])
            nums.remove(nums[0])  # remove 只会删除掉从头开始找到的第一个值
            i += 1
        return nums
#主函数
if __name__ == "__main__":
    nums = [4, 5, 1, 2, 3]
    #创建对象
    solution = Solution()
    print("输入的整数数组是 ：", nums)
    print("恢复的数组是:", solution.recoverRotatedSortedArray(nums))