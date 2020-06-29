class Solution:
    def maxPoints(self, points):
        if len(points) == 1:
            return 1
        max_count = 0
        for i in range(len(points)):  # 固定第一个点，第二个点在第一个点后，求所有可能的斜率
            xielv = dict()            # key 存斜率，val存出现的次数
            infinite = 0
            for j in range(i + 1, len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                if dx == 0:
                    infinite += 1
                    continue
                g = dy / dx
                xielv[g] = xielv[g] + 1 if g in xielv else 1  # 字典进行初始化
            for key in xielv.keys():
                max_count = max(max_count, xielv[key] + 1)   # +1 是算上第一个点本身
            max_count = max(infinite + 1, max_count)
        return max_count

# 主函数
if __name__ == '__main__':
    points = [[0,0],[1,1],[0,0]]
    solution = Solution()
    print("结果：", solution.maxPoints(points))
