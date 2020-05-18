class Solution():
    def move(self, A, B):
        print(A + '->' + B)

    def hanoi(self, n, A, B, C): # 将n个盘子经过B从A移到C
        if n == 1:
            self.move(A, C)
            return
        self.hanoi(n - 1, A, C, B) # 将n - 1个盘子经过C从A移到B
        self.move(A, C)
        self.hanoi(n - 1, B, A, C) # 将n - 1个盘子经过A从B移到C


if __name__ == "__main__":
    tow1, tow2, tow3 = [], [], []
    n = 3
    for i in range(n - 1, -1, -1):
        tow1.append(i)
    solution = Solution()
    # solution.hanoi(n, tow1, tow2, tow3)
    # print(tow3)
    solution.hanoi(n, 'A', 'B', 'C')