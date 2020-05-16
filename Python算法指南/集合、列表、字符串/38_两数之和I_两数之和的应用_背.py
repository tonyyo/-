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

    def twoSum2(self, nums, target):
        hash = {} # hash映射
        ans = [] # 存储所有可能结果值
        for i in range(len(nums)):
            if target - nums[i] in hash:
                ans.append([hash[target - nums[i]], i])
            hash[nums[i]] = i
        return ans

if __name__ == '__main__':
    temp = Solution()
    List = [5, 4, 3, 4, 11]
    nums = 8
    print(("输入：" + str(List) + "  " + str(nums)))
    print(("输出：" + str(temp.twoSum(List, nums))))
    print(("输出：" + str(temp.twoSum2(List, nums))))
