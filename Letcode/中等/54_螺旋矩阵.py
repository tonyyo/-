class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        if len(matrix) == 0:
            return []
        M, N = len(matrix), len(matrix[0])
        visit = [[0] * N for _ in range(M)]
        res = []
        x, y = 0, 0
        res.append(matrix[0][0])
        visit[0][0] = 1
        direct = 0
        while len(res) < M * N:
            nextX, nextY = x + dx[direct], y + dy[direct]
            if not self.inbound(matrix, nextX, nextY) or visit[nextX][nextY] == 1:
                if direct == 0:
                    x += 1
                elif direct == 1:
                    y -= 1
                elif direct == 2:
                    x -= 1
                else:
                    y += 1
                direct = (direct + 1) % 4
            else:
                x, y = nextX, nextY
            res.append(matrix[x][y])
            visit[x][y] = 1
        return res

    def inbound(self, matrix, x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

if __name__ == '__main__':
    solution = Solution()
    matrix = [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    print(solution.spiralOrder(matrix))