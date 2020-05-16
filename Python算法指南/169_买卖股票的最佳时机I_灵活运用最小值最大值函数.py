import sys


class Solution:
    def maxProfit2(self, prices):
        total = 0
        low, high = sys.maxsize, 0
        for x in prices:
            if x - low > total:
                total = x - low
            if x < low:
                low = x
        return total

    def maxProfit(self, prices): # 前n个数中取最小值, 然后用后n个数中的一个减去最小值,然后更新最大利润
        total = 0
        prefix_lowest = prices[0]
        for i in range(1, len(prices)):
            total = max(total, prices[i] - prefix_lowest)
            prefix_lowest = min(prices[i], prefix_lowest)
        return total




if __name__ == '__main__':
    temp = Solution()
    nums1 = [3, 2, 3, 1, 2]
    nums2 = [5, 3, 3, 4, 6]
    print(("输入：" + str(nums1)))
    print(("输出：" + str(temp.maxProfit(nums1))))
    print(("输入：" + str(nums2)))
    print(("输出：" + str(temp.maxProfit(nums2))))
