class Solution:
    def minimumTotal(self, triangle):
        res = [triangle[0]]
        N = len(triangle)
        for i in range(1, len(triangle)):
            res.append([])
            for j in range(len(triangle[i])):
                if j - 1 >= 0 and j < len(triangle[i - 1]):
                    res[i].append(min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j])
                elif j - 1 >= 0:
                    res[i].append(res[i - 1][j - 1] + triangle[i][j])
                else:
                    res[i].append(res[i - 1][j] + triangle[i][j])
        minvalue = min(res[N - 1])
        return minvalue

    def minimumTotal1(self, triangle):
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
    print("最小路径：", solution.minimumTotal1(triangle))