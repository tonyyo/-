import sys


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        maxProfit, minVal = 0, sys.maxsize
        for x in prices:
            minVal = min(minVal, x)
            maxProfit = max(maxProfit, x - minVal)
        return maxProfit