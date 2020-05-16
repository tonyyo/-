class Solution:
    def flipLights(self, n, m):
        if m == 0 or n == 0:
            return 1
        if n == 1:
            return 2
        elif n == 2:
            if m == 1:
                return 3
            elif m > 1:
                return 4
        elif n >= 3:
            if m == 1:
                return 4
            elif m == 2:
                return 7
            elif m > 2:
                return 8  # https://blog.csdn.net/zhaohengchuan/article/details/78697549
#主函数
if __name__ == '__main__':
    n = 2
    m = 1
    print("初始值：n={}，m={}".format(n, m))
    solution = Solution()
    print("结果：", solution.flipLights(n, m))