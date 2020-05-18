class Solution:
    def subsets2(self, nums):
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                result.append(nums[i : j])
        return result

#主函数
if __name__ == '__main__':
    nums = [1, 2, 3]
    print("整数集合是：", nums)
    solution = Solution()
    print("包含的所有子集有：", solution.subsets2(nums))