class Solution:
    def reverseArray(self, nums):
        start, end = 0, -1
        for i in range(len(nums) // 2):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums
#主函数
if __name__=="__main__":
    nums=[1,2,5,3,4,6,8,9]
    #创建对象
    solution=Solution()
    print("输入的数组是：",nums)
    print("翻转之后的结果是：",solution.reverseArray(nums))