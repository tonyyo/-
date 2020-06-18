import collections


class Solution:
    def surroundedRegions(self, board):
        rowNum, colNum = len(board), len(board[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        queue = collections.deque()
        for i in range(rowNum):
            if board[i][0] == 'O': # 第一列
                queue.append([i, 0])
            if board[i][colNum - 1] == 'O': # 最后一列
                queue.append([i, colNum - 1])
        for j in range(colNum):
            if board[0][j] == 'O': # 第一行
                queue.append([0, j])
            if board[rowNum - 1][j] == 'O': # 最后一行
                queue.append([rowNum - 1, j])
        while queue:
            x, y = queue.popleft()
            board[x][y] = 'T'  # 从queue中弹出后统一操作，效率更高
            for i in range(4):
                nextX, nextY = x + dx[i], y + dy[i]
                if not (0 <= nextX < rowNum and 0 <= nextY < colNum) or board[nextX][nextY] != 'O':
                    continue
                else:
                    queue.append([nextX, nextY])
        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'

# 主函数
if __name__ == '__main__':
    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]
    print("board形状是：", board)
    solution = Solution()
    solution.surroundedRegions(board)
    print("修改过后的形状是：", board)
