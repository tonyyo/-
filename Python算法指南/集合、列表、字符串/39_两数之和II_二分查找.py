class Solution:
    def twoSum2(self, nums, target):
        ans = []
        left, right = 0, len(nums) -1
        while left < right:
            temp = target - nums[left] # 两数之和都是像这样，遍历一个，然后用和减去这个得另一个，看是否存在。
            if temp == nums[right]:     # 等于了，存起来，往下接着找下一组
                ans.append([left, right])
                left += 1
                right -= 1
            elif temp < nums[right]: # 小于了，右指针往左走
                right -= 1
            else:                   # 大于了，左指针往右走
                left += 1
        return ans

# 主函数
if __name__ == "__main__":
    nums = [2, 3, 7, 8, 11, 15]
    target = 10
    # 创建对象
    solution = Solution()
    print("初始化的数组nums=", nums, "目标值target=", target)
    print(" 两个数的和等于目标值的下标是：", solution.twoSum2(nums, target))

# class Solution:
#     def twoSum(self, nums, target):
#         if not nums:
#             return []
#         left, right = 0, len(nums) - 1
#         while left < right:
#             res = target - nums[left]
#             if res == nums[right]:
#                 break
#             elif res < nums[right]:
#                 right -= 1
#             else:
#                 left += 1
#         if left == right:
#             return [-1, -1]
#         return [left + 1, right + 1]