class Solution:
    def canJump(self, A):
        N = len(A)
        maxPos = 0
        for i in range(N):
            if maxPos >= i and i + A[i] > maxPos:
                maxPos = i + A[i]  # 如果当前位置可达， 并且从该位置起跳能够达到的跳数大于最远距离
        return maxPos >= N - 1


if __name__ == '__main__':
    temp = Solution()
    List1 = [1, 1, 0, 2]
    List2 = [1, 2, 0, 1, 2, 1]
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.canJump(List1))))
