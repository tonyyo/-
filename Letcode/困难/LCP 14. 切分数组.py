import sys


class Solution(object):
    #todo 超时
    def splitArray(self, nums):
        N = len(nums)
        dp = [sys.maxsize] * N  # dp[i] 表示以nums[i]结尾能切分的数组能切分的最小子数组
        dp[0] = 1
        for i in range(len(dp)):
            for j in range(i):
                if self.gcd(nums[i], nums[j]) > 1:
                    if j == 0:  # 匹配到第一个，直接为1
                        dp[i] = 1
                    else:
                        dp[i] = min(dp[i], dp[j - 1] + 1)  # 比较所有可能情况的最小值，核心状态转移方程
            if dp[i] == sys.maxsize:  # 没有匹配到任何数
                dp[i] = dp[i - 1] + 1
        return dp[N - 1]

    def gcd(self, num1, num2):
        while num1 != 0:
            num1, num2 = num2 % num1, num1   # 只需要记住这样做能保证num2能够大于num1，所以要将num2 % num1的值赋给num1
        return num2

if __name__ == '__main__':
    solution = Solution()
    nums1 = [2,3,3,2,3,3]
    nums = [2,3,3,2,3,3]
    print(solution.splitArray(nums1))
