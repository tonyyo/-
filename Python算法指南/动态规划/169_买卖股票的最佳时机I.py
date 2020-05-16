import sys


class Solution:
    def maxProfit(self, prices):
        minPrice, maxLiRun = sys.maxsize, 0
        for i in range(len(prices)): # 一边记录最低价， 一边记录最大利润
            minPrice = min(minPrice, prices[i])
            maxLiRun = max(maxLiRun, prices[i] - minPrice)
        return maxLiRun



if __name__ == '__main__':
    temp = Solution()
    nums1 = [3, 2, 3, 1, 2]
    nums2 = [5, 3, 3, 4, 6]
    print(("输入：" + str(nums1)))
    print(("输出：" + str(temp.maxProfit(nums1))))
    print(("输入：" + str(nums2)))
    print(("输出：" + str(temp.maxProfit(nums2))))
