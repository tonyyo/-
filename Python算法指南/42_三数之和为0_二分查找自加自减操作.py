class Solution:
    def threeSum(self, nums):
        nums.sort()
        results = []
        length = len(nums)
        for i in range(length - 2):  # 把i当做第一个数,再后面取两个数, 防止取三个数会出现重复取数的情况
            target = -nums[i]
            if i and nums[i] == nums[i - 1]:  # 负数会索引到后面, 所以不用担心
                continue
            left, right = i + 1, length - 1
            while left < right:  # 这种left和right自加自减的, 直接left <　right就好，　因为在判断的基础上自加和自减了
                sum = nums[left] + nums[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        return results

if __name__ == '__main__':
    temp = Solution()
    List1 = [-1, -1, 1, 1, 2, -2]
    List2 = [3, 0, 2, -5, 1]
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.threeSum(List1))))
    print(("输入：" + str(List2)))
    print(("输出：" + str(temp.threeSum(List2))))

# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         results = []
#         length = len(nums)
#         for i in range(0, length - 2):  # 因为是三个数, i后面可能存在两个数的情况, 所以时Length - 2
#             if i and nums[i] == nums[i - 1]:  # 因为进行了排序, 所以如果两个相邻的数相等的话, 就跳过
#                 continue
#             target = -nums[i]   # 取符号构造等式
#             left, right = i + 1, length - 1
#             while left < right:
#                 if nums[left] + nums[right] == target:
#                     results.append([nums[i], nums[left], nums[right]])
#                     right -= 1
#                     left += 1
#                     while left < right and nums[left] == nums[left - 1]:  #因为左右指针都进行了移动, 如果相邻的数是一样的, 那么没有必要进行比较,跳过去就好,只是这里不是用的continue
#                         left += 1
#                     while left < right and nums[right] == nums[right + 1]:
#                         right -= 1
#                 elif nums[left] + nums[right] > target:
#                     right -= 1
#                 else:
#                     left += 1
#         return results