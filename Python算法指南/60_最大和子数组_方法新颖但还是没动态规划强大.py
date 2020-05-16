import sys
class Solution:
    def maxSubArray(self, nums):
        a = nums[:]
        aa = nums[:]  # 声明为空数组的话只能用append, 不能用索引赋值
        for i in range(1, len(nums)):
            a[i] = max(a[i - 1] + nums[i], nums[i])  # 前n项中子数组最大和
            aa[i] = max(aa[i-1], a[i])
        return aa[len(aa) - 1]

if __name__ == '__main__':
    temp = Solution()
    nums2 = [4,2,1,4,-1,2,7,4,-3]
    print ("输出："+str(temp.maxSubArray(nums2)))

# import sys
# class Solution:
#     def maxSubArray(self, nums):
#         min_sum, max_sum = 0, -sys.maxsize
#         prefix_sum = 0
#         for num in nums:
#             prefix_sum += num  # 求出前n项和
#             min_sum = min(min_sum, prefix_sum) #找到最小和数组
#             max_sum = max(max_sum, prefix_sum - min_sum)  # 前n项和减去上次找到的最小和数组等于目前最大和子数组
#         return max_sum