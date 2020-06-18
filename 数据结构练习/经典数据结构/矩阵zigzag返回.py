class Solution:
    def printZMatrix(self, matrix):
        x, y= 0, 0
        M, N = len(matrix), len(matrix[0])
        dx, dy = [-1, 1], [1, -1]
        res = [matrix[0][0]]
        direct = 0
        while len(res) < M * N:
            nextX, nextY = x + dx[direct], y + dy[direct]
            if not (0 <= nextX < M and 0 <= nextY < N):
                if direct == 0:
                    if nextY >= N:
                        x += 1
                    else:
                        y += 1
                    direct = 1
                else:
                    if nextX >= M:
                        y += 1
                    else:
                        x += 1
                    direct -= 1
            else:
                x, y = nextX, nextY
            res.append(matrix[x][y])
        return res

# 主函数
if __name__ == "__main__":
    matrim = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    # 创建对象
    solution = Solution()
    print("输入的数组为：", matrim)
    print("ZigZag顺序返回矩阵的所有元素是：", solution.printZMatrix(matrim))