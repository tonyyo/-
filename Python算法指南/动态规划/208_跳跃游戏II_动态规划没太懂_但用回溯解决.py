class Solution:
    def jump(self, A):
        p = [0] # p[i]表示跳到i这个位置最少需要多少步
        for i in range(len(A) - 1):
            while (i + A[i] >= len(p) and len(p) < len(A)): # 后面那个条件保证只跳到最后一个位置，不会往后跳了。
                p.append(p[i] + 1)  # 使p的长度延长到跳跃到的那个位置，非常巧妙
        return p[-1]

    def jump2(self, A):
        p = [0] # 必须要有一个元素，因为p的赋值会依赖上一个元素，因为p[i]的涵义是跳到i这个位置是最少需要多少步。
        for i in range(len(A)):
            while (i + A[i] >= len(p) and len(p) < len(A)): # 当p中的元素等于A时，外层循环将是一个空壳
                p.append(p[i] + 1)
        return p[-1]


    # 我的回溯解法
    def huisuJump(self, A, steps, result, start):
        if start >= len(A) - 1: # 出口为跳出边界
            result.append(steps)
            return
        for i in range(A[start], 0, -1): # 回溯跳跃的步数，最小为1
            steps += 1
            self.huisuJump(A, steps, result, start + i)
            steps -= 1


if __name__ == '__main__':
    temp = Solution()
    List2 = [1, 3, 5, 2, 1, 3, 1, 1]
    steps, result, start = 0, [], 0
    print(("输入：" + str(str(List2))))
    print(temp.jump2(List2))
