class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        row, col, box = [[] for _ in range(9)], [[] for _ in range(9)], [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row[i]:
                        return False
                    elif board[i][j] in col[j]:
                        return False
                    elif board[i][j] in box[(i // 3) * 3 + (j // 3)]:
                        return False
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                    box[(i // 3) * 3 + (j // 3)].append(board[i][j])
        return True
if __name__ == '__main__':
    solution = Solution()
    board = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    print(solution.isValidSudoku(board))
