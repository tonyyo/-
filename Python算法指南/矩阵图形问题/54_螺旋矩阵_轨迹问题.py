#参数matrix是mxn的矩阵
#返回值是一个整数数组
class Solution:
     def spiralOrder(self, matrix):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        direct = 0
        rowNum, colNum = len(matrix), len(matrix[0])
        visit = [[0 for _ in range(colNum)] for _ in range(rowNum)]
        visit[0][0] = 1
        result = [matrix[0][0]]
        x, y = 0, 0
        for i in range(rowNum * colNum - 1): # 因为已经记录了第一个点
            nextX, nextY = x + dx[direct], y + dy[direct]
            if 0 <= nextX < rowNum and 0 <= nextY < colNum and visit[nextX][nextY] == 0:
                x, y = nextX, nextY
            else:
                if direct == 0: # 方向向右
                    x = x + 1
                    direct = 1
                elif direct == 1:
                    y = y - 1
                    direct = 2
                elif direct == 2:
                    x = x - 1
                    direct = 3
                else:
                    y = y + 1
                    direct = 0
            result.append(matrix[x][y])  # 确定好下一步的位置后，走到下一步，并将其存起来
            visit[x][y] = 1 # 沿途记下经过的点
        return result




#主函数
if __name__=="__main__":
    arr = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
    #创建对象
    solution=Solution()
    print("输入的数组是：", arr)
    print("螺旋顺序顺出后的矩阵是：",solution.spiralOrder(arr))