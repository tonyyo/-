class Solution:
    def minimumTotal(self, triangle):
        rowNum = len(triangle)
        for i in range(1, rowNum):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        return min(triangle[rowNum - 1])

#主函数
if __name__ == '__main__':
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print("初始数字三角形：")
    for i in range(0,len(triangle)):
        print(triangle[i])
    solution = Solution()
    print("最小路径：", solution.minimumTotal(triangle))