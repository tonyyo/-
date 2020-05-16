from itertools import combinations


class Solution:
    def threeSum(self, nums):
        nums.sort() # 需排序
        results = []
        length = len(nums)
        for i in range(length - 2):  # 后面留两个数
            target = -nums[i]        # 因为三数之和等于0，相当于0 - nums[i]
            if i and nums[i] == nums[i - 1]:  # 负数会索引到后面, 所以不用担心
                continue
            left, right = i + 1, length - 1 # 因为是排序的，所以可以这么做。
            while left < right:
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

    def threeSum2(self, nums):
        tempList = list(combinations(nums, 3))
        ans = []
        for x in tempList:
            if sum(x) == 0:
                ans.append(list(x)) # 将元组转化为列表
        return ans

if __name__ == '__main__':
    temp = Solution()
    List1 = [-1, -1, 1, 1, 2, -2]
    List2 = [3, 0, 2, -5, 1]
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.threeSum(List1))))
    print(("输出：" + str(temp.threeSum2(List1))))
    print(("输入：" + str(List2)))
    print(("输出：" + str(temp.threeSum(List2))))
    print(("输出：" + str(temp.threeSum2(List2))))

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