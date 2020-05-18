from itertools import combinations

class Solution:
    def subsets2(self, nums):
        result = []
        for i in range(len(nums) + 1):
            temp = list(combinations(nums, i))
            for x in temp:
                result.append(list(x)) # 将combinations的元组转化为列表。
        print(result)

#主函数
if __name__ == '__main__':
    nums = [1, 2, 3]
    print("整数集合是：", nums)
    solution = Solution()
    print("包含的所有子集有：", solution.subsets2(nums))