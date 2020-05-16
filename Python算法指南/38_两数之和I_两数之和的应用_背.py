class Solution(object):
    def twoSum(self, nums, target):
        hash = {0: 1}
        size = len(nums)
        ans = []
        for j in range(size):
            if target - nums[j] in hash:
                ans.append([hash[target - nums[j]], j])
            hash[nums[j]] = j
        return ans


if __name__ == '__main__':
    temp = Solution()
    List = [5, 4, 3, 4, 11]
    nums = 8
    print(("输入：" + str(List) + "  " + str(nums)))
    print(("输出：" + str(temp.twoSum(List, nums))))

# class Solution(object):
#     def twoSum(self, nums, target):
#         #hash用于建立数值到下标的映射
#         hash = {}
#         #循环nums数值，并添加映射
#         for i in range(len(nums)):
#             if target - nums[i] in hash:  #非常巧的一个方法, 将列表中的数一一建立映射, 直到和减去第二个数等于在hash里面的第一个数.
#                 return [hash[target - nums[i]], i]
#             hash[nums[i]] = i   #建立映射的关键语句
#         #无解的情况
#         return [-1, -1]
