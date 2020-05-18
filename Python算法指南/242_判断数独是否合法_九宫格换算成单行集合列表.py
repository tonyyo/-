class Solution:
    def isValidSudoku1(self, board):
        row = [set([]) for i in range(9)]
        col = [set([]) for i in range(9)]
        grid = [set([]) for i in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False
                g = r // 3 * 3 + c // 3  # 将九个格子放在了一行
                if board[r][c] in grid[g]:
                    return False
                grid[g].add(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])
        return True

    def isValidSudoku(self, board):
        rowNum = len(board)
        colNum = len(board[0])
        row = [set([]) for _ in range(rowNum)]
        col = [set([]) for _ in range(colNum)]
        grid = [set([]) for _ in range(9)]
        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in row[i]:
                    return False
                elif board[i][j] in col[j]:
                    return False
                g = i // 3 * 3 + j // 3
                if board[i][j] in grid[g]:
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                grid[g].add(board[i][j])
        return True

# 主函数
if __name__ == "__main__":
    board = [".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........",
             "9........"]
    # 创建对象
    solution = Solution()
    print("初始值是：", board)
    print("结果是：", solution.isValidSudoku(board))
