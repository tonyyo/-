class Solution:
    def maxProduct(self, nums):
        MAX_JI = 0
        prefix_ji = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:         # 前一项和就等于第一项
                prefix_ji[i] = nums[i]
            elif prefix_ji[i - 1] >= 1:
                prefix_ji[i] = prefix_ji[i - 1] * nums[i]
            else:
                prefix_ji[i] = nums[i]
            MAX_JI = max(MAX_JI, prefix_ji[i])
        return MAX_JI
#主函数
if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    print("初始序列：", nums)
    solution = Solution()
    print("乘积最大子序列的积：", solution.maxProduct(nums))