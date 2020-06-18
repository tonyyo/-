class Solution:
    def solve(self, board: [[str]]) -> None:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        if len(board) == 0:
            return []
        M, N = len(board), len(board[0])
        import collections
        queue = collections.deque()
        for i in range(M):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][N - 1] == 'O':
                queue.append((i, N - 1))
        for j in range(N):
            if board[0][j] == 'O':
                queue.append((0, j))
            if board[M - 1][j] == 'O':
                queue.append((M - 1, j))
        while queue:
            x, y = queue.popleft()
            board[x][y] = 'T'
            for i in range(4):
                nextX, nextY = x + dx[i], y + dy[i]
                if not (0 <= nextX < M and 0 <= nextY < N) or board[nextX][nextY] != 'O':
                    continue
                queue.append((nextX, nextY))
        for i in range(M):
            for j in range(N):
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
    solution.solve(board)
    print("修改过后的形状是：", board)


