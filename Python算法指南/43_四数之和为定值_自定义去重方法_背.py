class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        length = len(nums)
        for i in range(length):
            result1 = target - nums[i]
            for j in range(i + 1, length):
                result2 = result1 - nums[j]
                left, right = j + 1, length - 1
                while left < right:
                    sum = nums[left] + nums[right]
                    if sum < result2:
                        left += 1
                    elif sum > result2:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
        result = []
        sorted(ans)
        for i in range(len(ans) - 1):
            while i + 1 < len(ans) and ans[i] == ans[i + 1]:  # 去重
                i = i + 1
            result.append(ans[i])
        return result

if __name__ == '__main__':
    temp = Solution()
    List1 = [1, 2, 3, 4, 5, 1]
    nums1 = 10
    print(("输入：" + str(List1) + "  " + str(nums1)))
    print(("输出：" + str(temp.fourSum(List1, nums1))))

# class Solution(object):
#     def fourSum(self, nums, target):
#         nums.sort()
#         res = []
#         length = len(nums)
#         for i in range(0, length - 3):
#             if i and nums[i] == nums[i - 1]:  #第一个数和第二个数相等
#                 continue
#             for j in range(i + 1, length - 2):
#                 if j != i + 1 and nums[j] == nums[j - 1]: #第二个数和第三个数相等
#                     continue
#                 sum = target - nums[i] - nums[j]
#                 left, right = j + 1, length - 1
#                 while left < right:
#                     if nums[left] + nums[right] == sum:
#                         res.append([nums[i], nums[j], nums[left], nums[right]])
#                         right -= 1
#                         left += 1
#                         while left < right and nums[left] == nums[left - 1]:
#                             left += 1
#                         while left < right and nums[right] == nums[right + 1]:
#                             right -= 1
#                     elif nums[left] + nums[right] > sum:
#                         right -= 1
#                     else:
#                         left += 1
#         return res
