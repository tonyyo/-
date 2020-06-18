import sys

class Solution:
    def maxProfit(self, prices):
        s1 = -sys.maxsize  # s1、s3持有股票，强制卖出进入下一个状态
        s2 = 0
        s3 = -sys.maxsize
        s4 = 0
        for p in prices:
            s1 = max(s1, -p)
            s2 = max(s2, s1 + p)
            s3 = max(s3, s2 - p)
            s4 = max(s4, s3 + p)
        return max(0, max(s2, s4))



    def maxProfit2(self, prices: [int]) -> int:
        maxProfit = 0
        N = len(prices)
        for j in range(N):
            leftMin, leftMaxProfit = sys.maxsize, 0
            rightMax, rightMaxProfit = 0, 0
            for i in range(j + 1):
                leftMin = min(leftMin, prices[i])
                leftMaxProfit = max(leftMaxProfit, prices[i] - leftMin)
            for k in range(N - 1, j - 1, -1):
                rightMax = max(rightMax, prices[k])
                rightMaxProfit = max(rightMaxProfit, rightMax - prices[k])
            maxProfit = max(maxProfit,leftMaxProfit + rightMaxProfit)
        return maxProfit

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([1,2,3,4,5]))
