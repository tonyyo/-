class Solution:
    def firstWillWin(self, n):
        return bool(n % 3)
if __name__ == '__main__':
    temp = Solution()
    n1 = 100
    n2 = 200
    print("输入："+str(n1))
    print(("输出："+str(temp.firstWillWin(n1))))
    print("输入："+str(n2))
    print(("输出："+str(temp.firstWillWin(n2))))