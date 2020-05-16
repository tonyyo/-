class Solution:
    def jump(self, A):
        p = [0]  #
        for i in range(len(A) - 1):
            while (i + A[i] >= len(p) and len(p) < len(A)):
                p.append(p[i] + 1)
        print(p)
        return p[-1]

    def huisuJump(self, A, steps, result, start):
        if start >= len(A) - 1:
            result.append(steps)
            return
        for i in range(A[start], 0, -1):
            steps += 1
            self.huisuJump(A, steps, result, start + i)
            steps -= 1


if __name__ == '__main__':
    temp = Solution()
    List2 = [1, 3, 5, 2, 1, 3, 1, 1]
    steps, result, start = 0, [], 0
    print(("输入：" + str(str(List2))))
    temp.huisuJump(List2, steps, result, start)
    print(result)
    print(min(result))
