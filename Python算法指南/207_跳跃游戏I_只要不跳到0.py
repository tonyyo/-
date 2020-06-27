class Solution:
    def canJump(self, A):
        max_instance = 0  # 初始化能到达的最远距离
        N = len(A)
        for k, v in enumerate(A):
            if max_instance >= k and k + v > max_instance: # 当前位置可达，更新最大跳数
                max_instance = k + v
        return max_instance >= N - 1

if __name__ == '__main__':
    temp = Solution()
    List1 = [1, 1, 0, 2]
    List2 = [1, 2, 0, 1, 2, 1]
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.canJump(List1))))
