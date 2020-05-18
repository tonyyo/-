import collections


class Solution:
    def majorityNumber2(self, nums, k):
        counts = {}
        max = 0
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > max:
                max = counts[num]
                majority = num
        return majority

    def majorityNumber(self, nums, k):
        counts = collections.Counter(nums)
        for key, val in counts.items():
            if counts[key] > len(nums) // k:
                return key
        return None

# 主函数
if __name__ == "__main__":
    nums = [3, 1, 2, 3, 2, 3, 3, 4, 4, 4]
    k = 3
    # 创建对象
    solution = Solution()
    print("输入的数组是： ", nums)
    print("输出的结果是：", solution.majorityNumber(nums, k))