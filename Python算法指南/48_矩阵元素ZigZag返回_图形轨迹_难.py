class Solution:
    def printZMatrix(self, matrix):
        x, y= 0, 0
        xLen = len(matrix[0])
        yLen = len(matrix)
        dx = [-1, 1]
        dy = [1, -1]
        ans = [matrix[x][y]]
        direct = 1
        for i in range(xLen * yLen - 1):  # 因为提前加入了一个元素, 所以长度减1
            nextX = x + dx[direct]
            nextY = y + dy[direct]
            if nextX >= 0 and nextX < xLen and nextY >= 0 and nextY < yLen:
                x = x + dx[direct]
                y = y + dy[direct]
                ans.append(matrix[y][x])
            else:
                if direct == 1:
                    if nextY < 0:
                        x = x + 1
                        ans.append(matrix[y][x])
                    else:
                        y = y + 1
                        ans.append(matrix[y][x])
                    direct = 0
                else:
                    if nextX < 0:
                        y = y + 1
                        ans.append(matrix[y][x])
                    else:
                        x = x + 1
                        ans.append(matrix[y][x])
                    direct = 1
        return ans
# 主函数
if __name__ == "__main__":
    matrim = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # 创建对象
    solution = Solution()
    print("输入的数组为：", matrim)
    print("ZigZag顺序返回矩阵的所有元素是：", solution.printZMatrix(matrim))

# class Solution:
#     def printZMatrix(self, matrix):
#         if len(matrix) == 0:
#             return []
#         x, y = 0, 0
#         n, m = len(matrix), len(matrix[0])
#         rows, cols = range(n), range(m)
#         dx = [1, -1]  #x的左右方向
#         dy = [-1, 1]  #y的上下方向
#         direct = 1    # 1 = 左下方移动, 0 = 右上方移动,
#         result = []   #轨迹上的点序
#         for i in range(len(matrix) * len(matrix[0])):  # 循环二维列表
#             result.append(matrix[x][y])
#             nextX = x + dx[direct] # 试探
#             nextY = y + dy[direct]
#             if nextX not in rows or nextY not in cols: # 当x和y都在集合中时, 不需要进入该判断条件
#                 if direct == 1:  #左下方移动, 只有可能, 左边小于0, 下面超出范围.
#                     if nextY >= m:  # m是最大行号
#                         nextX, nextY = x + 1, y # 向左下移动超过最大行, 则向右横向移动
#                     else:
#                         nextX, nextY = x, y + 1 # 否则, 向下移动
#                 else:
#                     if nextX >= n:  # n是最大列号
#                         nextX, nextY = x, y + 1  # 向右上移动超过最大列, 则向下移动
#                     else:
#                         nextX, nextY = x + 1, y  #否则, 向右移动
#                 direct = 1 - direct  # 超出列表的最大行数或列数, 改变方向
#             x, y = nextX, nextY
#         return result