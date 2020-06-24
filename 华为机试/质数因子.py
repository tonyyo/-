class Solution():
    def findZhi(self, n):  # 超时
        N = n
        if n == 1 or n == 2:
            print(n, end=" ")
        while n != 1:
            for i in range(2, N):
                if n % i == 0:  # 找到一个质因子
                    print(i, end=" ")
                    n = n // i
                    break

    def findZhi(self, n):  # 找n的质因子
        flag = True  # 设置标志，看是否到了最后一个质因子
        for i in range(2, n):
            if n % i == 0:  # 找到一个质因子
                print(i, end=" ")
                self.findZhi(n // i)
                flag = False
                break  # 找到了不再找了
        if flag:
            print(n, end=" ")   # 这是一个不回溯的递归，用来打印


if __name__ == '__main__':
    n = int(input())  # input()接收的是字符串
    solution = Solution()
    solution.findZhi(n)