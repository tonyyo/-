import sys


class Solution:
    def integerReplacement(self, n):
        self.len = sys.maxsize
        self.dfs(n, [n])
        return self.len - 1

    def dfs(self, n, temp):  # temp记录沿途情况，以便记录替换次数
        if n == 1:
            self.len = min(self.len, len(temp))
            return
        if n % 2 == 0:
            temp.append(n // 2)
            self.dfs(n // 2, temp)  # 一种情况，不存在回溯
        else:
            for x in [-1, 1]:  # 回溯n + 1和n - 1两种情况
                self.dfs(n + x, temp + [n + x])

if __name__ == '__main__':
    solution = Solution()
    print("输出:", solution.integerReplacement(18))
