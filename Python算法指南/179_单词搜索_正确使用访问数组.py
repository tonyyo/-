class Solution:
    def exist1(self, board, word):
        if word == []:
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        # 访问矩阵
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if self.exist2(board, word, visited, i, j):
                    return True
        return False

    def exist2(self, board, word, visited, row, col):
        if word == '':
            return True
        m, n = len(board), len(board[0])
        if row < 0 or row >= m or col < 0 or col >= n:
            return False
        if board[row][col] == word[0] and not visited[row][col]:
            visited[row][col] = True
            # row - 1, col
            if self.exist2(board, word[1:], visited, row - 1, col) or self.exist2(board, word[1:], visited, row,
                                                                                  col - 1) or self.exist2(board,
                                                                                                          word[1:],
                                                                                                          visited,
                                                                                                          row + 1,
                                                                                                          col) or self.exist2(
                board, word[1:], visited, row, col + 1):
                return True
            else:
                visited[row][col] = False
        return False

    def exist(self, board, word):
        rowNum = len(board)
        colNum = len(board[0])
        size = len(word)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        result = []
        self.findInit(board, word[0], result)
        for init in result:  # 起始坐标
            x = init[0]
            y = init[1]
            # visit = [[False for _ in range(colNum)]  for _ in range(rowNum)]  # 必须在这个地方初始化
            visit = [[False] * colNum for _ in range(rowNum)]
            visit[x][y] = True
            count = 0
            for i in range(1, size): # 从第二个字母开始比较
                flag = False
                for j in range(4):
                    nextX = x + dx[j]
                    nextY = y + dy[j]
                    if nextX >= 0 and nextY >=0 and nextX < rowNum and nextY < colNum and visit[nextX][nextY] == False:
                        if board[nextX][nextY] == word[i]:
                            x, y = nextX, nextY
                            visit[x][y] = True
                            flag = True
                            count += 1
                            break    # 如果找到了对应的字母, 也直接跳出, 不再比较其他方向, 这似乎有点问题, 如果要求出多个解的话
                if flag == False:  # 如果一个字母不同, 那么直接跳出,不再比较后面的字母, 而重新找一个开头
                    break
            if count == size - 1:
                return True
        return False

    def findInit(self, board, initAlpha, result):
        rowNum = len(board)
        colNum = len(board[0])
        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] == initAlpha:
                    result.append([i, j])

# 主函数
if __name__ == '__main__':
    board = ["ABCE", "SFCS", "ADEE"]
    word1 = "ABCCED"
    word2 = "ABCESEEDAS"
    solution = Solution()
    print("board是：", board)
    print("word1是：", word1, ",结果是：", solution.exist(board, word1))
    print("word2是：", word2, ",结果是：", solution.exist(board, word2))
