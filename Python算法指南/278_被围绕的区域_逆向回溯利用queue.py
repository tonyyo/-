import collections


class Solution:
    def surroundedRegions1(self, board):
        if not any(board):
            return
        n, m = len(board), len(board[0])
        q = [ij for k in range(max(n, m)) for ij in ((0, k), (n - 1, k), (k, 0), (k, m - 1))]
        while q:
            i, j = q.pop()
            if 0 <= i < n and 0 <= j < m and board[i][j] == 'O':
                board[i][j] = 'W'
                q += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)
        board[:] = [['XO'[c == 'W'] for c in row] for row in board]

    def surroundedRegions(self, board):
        rowNum = len(board)
        colNum = len(board[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(rowNum):
            for j in range(colNum):
                if i == 0 or j == 0 or i == rowNum - 1 or j == colNum - 1:
                    if board[i][j] == 'O':
                        queue = collections.deque()
                        queue.append((i, j))
                        board[i][j] = 'T'
                        while queue:
                            x, y = queue.popleft()
                            for k in range(4):
                                nextX = x + dx[k]
                                nextY = y + dy[k]
                                if not (0 <= nextX < rowNum and 0 <= nextY < colNum) or board[nextX][nextY] != 'O':
                                    continue
                                queue.append((nextX, nextY))
                                board[nextX][nextY] = 'T'

        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'
        return board


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
