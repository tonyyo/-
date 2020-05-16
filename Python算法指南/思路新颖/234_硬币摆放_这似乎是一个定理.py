import math
class Solution:
    def arrangeCoins(self, n):
        return math.floor((-1 + math.sqrt(1 + 8*n)) / 2) # 根据等差数列求和，计算x的大小

    def arrangeCoins1(self, n):
        ca = n
        for i in range(1, n):
            ca -= i
            if ca < 0:
                return i - 1 # 返回上一层的层数
        return -1

if __name__ == '__main__':
    temp = Solution()
    n1 = 5
    n2 = 10
    print(("输入："+str(n1)))
    print("输出："+str(temp.arrangeCoins(n1)))
    print("输出："+str(temp.arrangeCoins1(n1)))
    print(("输入："+str(n2)))
    print("输出："+str(temp.arrangeCoins(n2)))
    print("输出："+str(temp.arrangeCoins1(n2)))