# 一块土地n*m， 为保证果树存活， 0表示岩石， 1表示土壤， 不能种在岩石里， 不能相邻种植， 问有几种种植方式？
# 这种题型做的比较少
import sys
class Solution():
    count = 0
    def adjust(self, res):
        g, c = len(res), len(res[0])
        List = [[0 for _ in range(c + 1)] for _ in range(g + 1)]
        for i in range(1, g + 1):
            for j in range(1, c + 1):
                List[i][j] = res[i - 1][j - 1]
        self.dfs(List, 1, 1)
        return self.count

    def dfs(self, res, x, y):
        if x >= len(res) - 1 or y >= len(res[0]) - 1:
            self.count += 1
            return
        if res[x][y] == 0:
            self.go(res, x, y)
        if res[x][y] == 1:
            if not (res[x-1][y] != 2 and res[x][y-1] != 2):
                self.go(res, x, y)
            else:
                for k in range(2):
                        if k == 0:
                            self.go(res, x, y)
                        else:
                            res[x][y] = 2
                            self.go(res, x, y)
                            res[x][y] = 1

    def go(self, res, x, y):
        if y + 1 >= len(res[0]):
            self.dfs(res, x + 1, 1)
        else:
            self.dfs(res, x, y + 1)



if __name__ == "__main__":
    # 读取第一行的n
    strip = sys.stdin.readline().strip()
    n, m = strip[0], strip[1]
    ans = 0
    res = []
    for i in range(int(n)):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        values.insert(0, 0)
        res.append(values)
    solution = Solution()
    result = solution.adjust(res)
    print(result)