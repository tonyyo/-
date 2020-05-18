class Solution:
    def houseRobber(self, A):
        result = 0
        f, g, f1, g1 = 0, 0, 0, 0
        for x in A:
            f1 = g + x
            g1 = max(f, g)
            g, f = g1, f1
        return max(f, g)
#主函数
if __name__ == '__main__':
    A = [3, 8, 4]
    print("房屋存放金钱：", A)
    solution = Solution()
    print("打劫到的最多金钱：", solution.houseRobber(A))