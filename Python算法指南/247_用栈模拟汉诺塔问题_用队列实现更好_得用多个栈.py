class Solution():
    def hannoi2(self, tow1, tow2, tow3):  # 从tow1通过tow2到tow3
        if len(tow1) == 1:
            tow3.append(tow1.pop())
            return
        temp, tempTow = self.popleft(tow1)
        self.hannoi2(tempTow, tow3, tow2)
        tow3.append(temp)
        self.hannoi2(tow2, tempTow, tow3)

    def popleft(self, stack1):
        i = 0
        stack2 = []
        stack3 = []
        while len(stack1) > 0:
            stack2.append(stack1.pop())
        top = stack2.pop()
        while len(stack2) > 0:
            stack3.append(stack2.pop())
        return top, stack3

    def hannoi(self, n, A, B, C):
        if n == 1:
            self.move(A, C)
            return
        x = n - 1
        self.hannoi(x, A, C, B)
        self.move(A, C)
        self.hannoi(x, B, A, C)

    def move(self, A, B):
        print(A + "->" + B)

if __name__ == "__main__":
    tow1, tow2, tow3 = [], [], []
    n = 3
    for i in range(n - 1, -1, -1):
        tow1.append(i)
    print(tow1)
    solution = Solution()
    # solution.hannoi(n, 'A', 'B', 'C')
    solution.hannoi2(tow1, tow2, tow3)
    print(tow3)