class Solution:
    def maxProfit(self, prices: [int]) -> int:
        low, high = 0, 0  # 高价和低价指针
        N = len(prices)
        sum = 0
        for i in range(1, N):
            if prices[i] >= prices[high]:
                high = i
            else:
                sum += prices[high] - prices[low]
                low, high = i, i
        return prices[high] - prices[low] + sum
