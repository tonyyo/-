class Solution:
    def solveNQueens(self, N: int) -> [[str]]:
        result = []
        self.queenSettle(N, 0, 0, 0, 0, [], result)
        return result

    def queenSettle(self, N, row, column, pie, na, temp, result):
        if row >= N:
            result.append(temp[:])
            return
        bits = (~(column | pie | na)) & ((1 << N) - 1)  # 为1的位置可放置皇后
        while bits > 0: # 当为0时表明没有地方可以放置皇后，需要回溯
            p = bits & -bits  # 每次从当前行可用的各自中取出最右边为1的各自放置皇后
            str = bin(p)[2:].replace('1', 'Q').replace("0", ".", N-1)
            if len(str) < N:
                str = "." * (N - len(str)) + str
            temp.append(str)
            self.queenSettle(N, row + 1, column | p, (pie | p) << 1, (na | p) >> 1, temp, result)
            temp.pop()
            bits = bits & (bits - 1)  # 当前行的最右边各自已经选完了，将其置成0， 代表这个格子已被遍历过。
if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(4))
