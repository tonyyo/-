class Solution:
    def subarraySum(self, nums):
        prefix_sum = 0
        prefix_hash = {0: -1}
        ans = []
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum in prefix_hash:
                ans.append([prefix_hash[prefix_sum] + 1, i])  # 依次计算前n项和,当前i项和与前j项和相等时, 表明[i+1,j-1]之间的子数组和为0
            prefix_hash.update({prefix_sum: i})
        return ans

    def subarraySum2(self, nums):
        size = len(nums)
        ans = []
        for i in range(1, size + 1):
            for j in range(size - i + 1):
                sum = 0
                for k in range(j, j + i):
                    sum += nums[k]
                if sum == 0:
                    ans.append([j, j + i - 1])
        return ans
# 主函数


if __name__ == "__main__":
    nums = [-3, 1, 2, -3, 4]
    # 创建对象
    solution = Solution()
    print("初始化的数组是：", nums)
    print("和为零的子数组是：", solution.subarraySum(nums))

# class Solution:
#     def subarraySum(self, nums):
#         prefix_hash = {0: -1}
#         prefix_sum = 0
#         for i, num in enumerate(nums):
#             prefix_sum += num
#             if prefix_sum in prefix_hash:  # 因为和都是累加的, 当加上一个数等于之前的和时, 那么就会等于0
#                 return prefix_hash[prefix_sum] + 1, i
#             prefix_hash[prefix_sum] = i
#         return -1, -1
