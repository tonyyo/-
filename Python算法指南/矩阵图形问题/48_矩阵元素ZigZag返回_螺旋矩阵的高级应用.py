class Solution:
      def printZMatrix(self, matrix):
        dx = [-1, 1]
        dy = [1, -1]
        direct = 0
        rowNum, colNum = len(matrix), len(matrix[0])
        result = [matrix[0][0]]
        x, y = 0, 0
        for i in range(rowNum * colNum -1):
            nextX, nextY = x + dx[direct], y + dy[direct]
            if 0 <= nextX < rowNum and 0 <= nextY < colNum:
                x, y = nextX, nextY
            else:
                if direct == 0:
                    if nextX < 0 and nextY < colNum:
                        y = y + 1 # 只x越界，向右运动
                    else:
                        x = x + 1 # xy都越界或y越界，向下运动
                    direct = 1
                else:
                    if nextY < 0 and nextX < rowNum:
                        x = x + 1 # 只y越界，向下运动
                    else:
                        y = y + 1 # xy都越界 或 x越界，向右运动
                    direct = 0
            result.append(matrix[x][y]) # 确定好下一个位置的坐标后，存入结果数组
        return result


# 主函数
if __name__ == "__main__":
    matrim = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # 创建对象
    solution = Solution()
    print("输入的数组为：", matrim)
    print("ZigZag顺序返回矩阵的所有元素是：", solution.printZMatrix(matrim))
