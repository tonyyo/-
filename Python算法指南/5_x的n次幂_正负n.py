class Solution:
    def myPow(self, x, n1):   #在Python3中整除需使用"//"
        n = n1 if n1 > 0 else -n1
        pow = 1
        for _ in range(n):
            pow *= x
        return pow if n1 >= 0 else (1 / pow)

if __name__ == '__main__':
    temp = Solution()
    num1 = 2
    num2 = -2
    print(("输入："+str(num1)+"  "+str(num2)))
    print(("输出："+str(temp.myPow(num1,num2))))


