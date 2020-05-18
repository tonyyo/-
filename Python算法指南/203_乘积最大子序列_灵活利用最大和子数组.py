class Solution:
    def maxProduct2(self, nums):
        if not nums:
            return None
        global_max = prev_max = prev_min = nums[0]
        for num in nums[1:]:
            if num > 0:
                curt_max = max(num, prev_max * num)
                curt_min = min(num, prev_min * num)
            else:
                curt_max = max(num, prev_min * num)
                curt_min = min(num, prev_max * num)
            global_max = max(global_max, curt_max)
            prev_max, prev_min = curt_max, curt_min
        return global_max

    def maxProduct(self, nums):
        max_chengji = 1
        size = len(nums)
        result = []
        for i in range(size):
            max_chengji = max(max_chengji * nums[i], nums[i])
            result.append(max_chengji)
        print(result)
        return max(result)
#主函数
if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    print("初始序列：", nums)
    solution = Solution()
    print("乘积最大子序列的积：", solution.maxProduct(nums))