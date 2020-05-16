class Solution:
    def combine(self, n, k):
        self.res = []  # 用self修饰后就是全局变量了
        tmp = []
        self.dfs(n, k, 1, 0, tmp)
        return self.res
    def dfs1(self, n, k, m, p, tmp): # p用来计数k个数字, m用来实现递推
        if k == p:
            self.res.append(tmp[:])
            return
        for i in range(m, n + 1):
            tmp.append(i)
            self.dfs(n, k, i + 1, p + 1, tmp)
            tmp.pop()

    def dfs(self, n, k, m, p, tmp): # m用来递推后面的数
        if p == k:
            self.res.append(list(tmp))
            return    # 返回继续循环的条件
        for i in range(m, n + 1):
            tmp.append(i)
            self.dfs(n, k, i + 1, p + 1, tmp)
            tmp.pop()


#主函数
if __name__ == '__main__':
    n = 5
    k = 3
    solution = Solution()
    print("结果是：", solution.combine(n, k))