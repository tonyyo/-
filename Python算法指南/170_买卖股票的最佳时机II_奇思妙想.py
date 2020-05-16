import sys
class Solution:
    def maxProfit2(self, prices):
        total = 0
        low, high = sys.maxsize, sys.maxsize
        for x in prices:
            if x > high:
                high = x
            else:
                total += high - low
                high, low = x, x
        return total + high - low

    def maxProfit(self, prices):
        size = len(prices)
        total = 0
        low, high = prices[0], prices[0] # 为了满足尽可能多的交易, 那么遇到第一个就该直接买入, 看下一个是否比它大, 如果比他小,或者相等, 那么买入第二个
        for i in range(1, size):
            if prices[i] > high:
                high = prices[i]
            else:
                total += high - low
                high, low = prices[i], prices[i]
        return total + high - low  # 最后一次也要加上

if __name__ == '__main__':
    temp = Solution()
    nums1 = [2,1,2,0,1]
    nums2 = [5,3,3,4,6]
    print(("输入："+str(nums1)))
    print(("输出："+str(temp.maxProfit(nums1))))
    print(("输入："+str(nums2)))
    print(("输出："+str(temp.maxProfit(nums2))))