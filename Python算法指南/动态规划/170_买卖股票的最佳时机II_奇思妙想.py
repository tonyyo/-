import sys
class Solution:
    def maxProfit(self, prices):
        low, high, total = prices[0], prices[0], 0 # 高低两个指针，遇见高价高指针往上走，留下的低指针就是最低价
        for i in range(1, len(prices)):
            if int(prices[i]) > int(high):
                high = prices[i]   # 遇见高价就往上加，留在原地的low就是最低价
            else:
                total += high - low # 遇见了低价，赶忙抛售
                high, low = prices[i], prices[i] # 重新定义高低指针
        return total + high - low # 记得加上最后一次买卖

if __name__ == '__main__':
    temp = Solution()
    nums1 = [6,1,3,2,4,7]
    nums2 = [5,3,3,4,6]
    print(("输入："+str(nums1)))
    print(("输出："+str(temp.maxProfit(nums1))))
    print(("输入："+str(nums2)))
    print(("输出："+str(temp.maxProfit(nums2))))