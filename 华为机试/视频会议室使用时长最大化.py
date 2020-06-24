class Solution():
    def print(self, Tmx):
        for mx in Tmx:
            N = len(mx)
            mx = sorted(mx, key=lambda x : (x[0], -x[1]))
            self.Time = 0
            self.dfs(mx, 0, 8)
            print(self.Time)

    def dfs(self, mx, time, startTime):  # mx的最长使用时长
        N = len(mx)
        if N == 0:
            self.Time = max(self.Time, time)
            return
        for i in range(N):
            if mx[i][0] >= startTime:
                time += mx[i][1] - mx[i][0]
                self.dfs(mx[i + 1:], time, mx[i][1])
                time -= mx[i][1] - mx[i][0]

if __name__ == '__main__':
    solution = Solution()
    N = int(input())
    Tmx = []
    for _ in range(N):
        lineNum = int(input()) # 单行将一行数字存入列表
        mx = []          #  存储二维列表
        for _ in range(lineNum):
            string = input().strip()
            lineList = list(map(int, string.split()))
            mx.append(lineList)
        Tmx.append(mx)
    solution.print(Tmx)