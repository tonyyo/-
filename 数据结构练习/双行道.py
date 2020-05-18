class Solution():
    direct = [[0, 1], [1, 1], [-1, 1]]
    def road(self, mx, x, y, result):
        if x == 1 and y == len(mx[0]) - 1:
            result.append(1)
            return
        else:
            for i in range(len(self.direct)):
                nextX = (x + self.direct[i][0]) % 2
                nextY = (y + self.direct[i][1]) % 2
                if mx[nextX][nextY] == 'X' or nextY >= len(mx[0]):
                    continue
                else:
                    x, y = nextX, nextY
                    self.road(mx, nextX, nextY, result)

if __name__ == '__main__':
    solution = Solution()
    mx = []
    # Length = int(input().strip())
    # for _ in range(2):
    #     string = input().strip()
    #     mx.append(string)
    result = []
    mx = ['..X.X', 'XX...']
    solution.road(mx, 0, 0, result)
    print(result)


