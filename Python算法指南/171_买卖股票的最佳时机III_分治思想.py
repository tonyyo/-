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
        size = len(prices)
        p1 = [0] * size # 记录某个位置前进行一次交易的最大利润
        p2 = [0] * size # 记录某个位置后进行一次交易的最大利润

        prefix_low = prices[0]
        for i in range(1, size):
            prefix_low = min(prefix_low, prices[i])
            p1[i] = max(p1[i - 1], prices[i] - prefix_low)

        postfix_high = prices[-1]
        for i in range(size - 2, -1, -1):
            postfix_high = max(postfix_high, prices[i])
            p2[i] = max(p2[i + 1], postfix_high - prices[i])

        print(p1)
        print(p2)

        max_profit = 0
        for i in range(size):
            max_profit = max(max_profit, p1[i] + p2[i])
        return max_profit


if __name__ == '__main__':
    temp = Solution()
    nums1 = [2,1,3,5,5,3,2,1]
    print ("输入："+str(nums1))
    print ("输出："+str(temp.maxProfit(nums1)))

    # [0, 0, 2, 4, 4, 4, 4, 4]
    # [4, 4, 2, 0, 0, 0, 0, 0]