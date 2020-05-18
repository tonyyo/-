#参数matrix是mxn的矩阵
#返回值是一个整数数组
class Solution:
    def spiralOrder(self, matrix):
        ans = []
        rowNum, colNum = len(matrix), len(matrix[0])
        bool = [[False for _ in range(colNum + 1)] for _ in range(rowNum + 1)]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]  # 方向对应于右,下,左,上
        direct = 0
        x, y = 0, 0
        ans.append(matrix[x][y])
        bool[x][y] = True
        for _ in range(rowNum * colNum - 1):
            nextX = x + dx[direct]
            nextY = y + dy[direct]
            if nextX < rowNum and nextX >= 0 and nextY < colNum and nextY >= 0 and bool[nextX][nextY] == False:
                x, y = nextX, nextY
                ans.append(matrix[x][y])
            else:
                if direct == 0:
                    x += 1
                    ans.append(matrix[x][y])
                elif direct == 1:
                    y -= 1
                    ans.append(matrix[x][y])
                elif direct == 2:
                    x -= 1
                    ans.append(matrix[x][y])
                else:
                    y += 1
                    ans.append(matrix[x][y])
                bool[x][y] = True
                direct = (direct + 1) % 4
        return ans

#主函数
if __name__=="__main__":
    arr = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ],[10, 11, 12]]
    #创建对象
    solution=Solution()
    print("输入的数组是：", arr)
    print("螺旋顺序顺出后的矩阵是：",solution.spiralOrder(arr))

# class Solution:
#     def spiralOrder(self, matrix):
#         if matrix == []: return []
#         up = 0
#         left = 0
#         down = len(matrix) - 1
#         right = len(matrix[0]) - 1 # 行列的两个起点和两个终点
#         direct = 0  # 0: 向右 1:向下 2:向左 3:向上
#         res = []
#         while True:
#             if direct == 0:
#                 for i in range(left, right + 1):
#                     res.append(matrix[up][i])
#                 up += 1
#             if direct == 1:
#                 for i in range(up, down + 1):
#                     res.append(matrix[i][right])
#                 right -= 1
#             if direct == 2:
#                 for i in range(right, left - 1, -1):
#                     res.append(matrix[down][i])
#                 down -= 1
#             if direct == 3:
#                 for i in range(down, up - 1, -1):
#                     res.append(matrix[i][left])
#                 left += 1
#             if up > down or left > right: return res
#             direct = (direct + 1) % 4
# #主函数