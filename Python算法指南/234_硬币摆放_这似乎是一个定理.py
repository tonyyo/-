import math
class Solution:
    def arrangeCoins(self, n):
        return math.floor((-1 + math.sqrt(1 + 8*n)) / 2)
if __name__ == '__main__':
    temp = Solution()
    n1 = 5
    n2 = 10
    print(("输入："+str(n1)))
    print("输出："+str(temp.arrangeCoins(n1)))
    print(("输入："+str(n2)))
    print("输出："+str(temp.arrangeCoins(n2)))