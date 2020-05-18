class Solution:
    def houseRobber(self, A):
        result = 0
        f, g, f1, g1 = 0, 0, 0, 0
        for x in A:
            f1 = g + x
            g1 = max(f, g)
            g, f = g1, f1
        return max(f, g)

    def houseRobber2(self, A):
        size = len(A)
        A.insert(0, 0)  # 打劫第0家房屋没有钱
        f = [0] * (size + 1) # 打劫第i家房子的抢的钱
        g = [0] * (size + 1) # 不打劫第i家房子抢的钱
        MAX = [0] * (size + 1) # 打劫前i家房子抢的钱，等于上面的更大值
        for i in range(1, size + 1):
            f[i] = MAX[i - 2] + A[i] # 如果打劫第i家房子，等于打劫前i-2家房子的最大值 + 第i家房子的钱
            g[i] = max(MAX[i - 1], MAX[i - 2]) # 如果不打劫第i家房子，那么最大值就是打劫前i - 2家和前 i - 1家房子的更大值。
            MAX[i] = max(f[i], g[i])
        print(MAX)
        return MAX[len(A) - 1]

#主函数
if __name__ == '__main__':
    A = [3, 8, 4, 5, 7]
    print("房屋存放金钱：", A)
    solution = Solution()
    print("打劫到的最多金钱：", solution.houseRobber2(A))