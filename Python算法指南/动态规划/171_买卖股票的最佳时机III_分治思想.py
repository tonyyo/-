import sys


class Solution:
    def maxProfit2(self, prices):  # https://www.jianshu.com/p/e46e98fa600d?tdsourcetag=s_pctim_aiomsg
        n = len(prices)
        if n <= 1:
            return 0
        p1 = [0] * n
        p2 = [0] * n
        minV = prices[0]
        for i in range(1,n):
            minV = min(minV, prices[i])
            p1[i] = max(p1[i - 1], prices[i] - minV)
        maxV = prices[-1]
        for i in range(n-2, -1, -1):
            maxV = max(maxV, prices[i])
            p2[i] = max(p2[i + 1], maxV - prices[i])
        res = 0
        print(p1)
        print(p2)
        for i in range(n):
            res = max(res, p1[i] + p2[i])
        return res

    def maxProfit(self, prices):
        p1 = [0] * len(prices) # 存的是i和i之间的最大交易额
        p2 = [0] * len(prices) # 存的是j和j之后的最大交易额

        minPrice1 = prices[0] # 以首尾元素为最大价格和最小价格
        for i in range(1, len(prices)):
            minPrice1 = min(minPrice1, prices[i])
            p1[i] = max(p1[i-1], prices[i] - minPrice1)  # 如果不用max，将是该点相比于最低价格的交易额

        maxPrice2 = prices[-1]
        for j in range(len(prices) - 2, -1, -1):
            maxPrice2 = max(maxPrice2, prices[j])
            p2[j] = max(p2[j+1], maxPrice2 - prices[j])

        maxLirun = 0
        for k in range(len(prices)):
            maxLirun = max(p1[k] + p2[k], maxLirun)
        return maxLirun



if __name__ == '__main__':
    temp = Solution()
    nums1 = [2,1,3,5,5,3,2,1]
    print ("输入："+str(nums1))
    print ("输出："+str(temp.maxProfit(nums1)))
    print ("输出："+str(temp.maxProfit2(nums1)))

    # [0, 0, 2, 4, 4, 4, 4, 4]
    # [4, 4, 2, 0, 0, 0, 0, 0]