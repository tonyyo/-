class Solution:
    def twoSum(self, nums, target):
        size = len(nums)
        left, right = 0, size - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return [left + 1, right + 1]
# 主函数
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 6
    # 创建对象
    solution = Solution()
    print("初始化的数组nums=", nums, "目标值target=", target)
    print(" 两个数的和等于目标值的下标是：", solution.twoSum(nums, target))

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