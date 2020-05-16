import sys
class Solution:
    def subarraySumClosest(self, nums):
        prefix_sum = [(0, -1)]
        for i, num in enumerate(nums):
            prefix_sum.append((prefix_sum[-1][0] + num, i))
        prefix_sum.sort()
        closest, answer = sys.maxsize, []
        for i in range(1, len(prefix_sum)):
            if closest > prefix_sum[i][0] - prefix_sum[i - 1][0]:
                closest = prefix_sum[i][0] - prefix_sum[i - 1][0]
                left = min(prefix_sum[i - 1][1], prefix_sum[i][1]) + 1
                right = max(prefix_sum[i - 1][1], prefix_sum[i][1])
                answer = [left, right]
        return answer
# 主函数
if __name__ == '__main__':
    nums = [-3, 1, 1, -3, 5]
    print("初始数组：", nums)
    solution = Solution()
    print("结果：", solution.subarraySumClosest(nums))