class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints1(self, points):
        max_count = 0
        for i in range(len(points)):
            xielv = {}
            infinite = 0
            for j in range(i + 1, len(points)):
                dx = points[i].x - points[j].x
                dy = points[i].y - points[j].y
                if dx == 0:
                    infinite += 1
                    continue
                g = dy / dx
                xielv[g] = xielv[g] + 1 if g in xielv else 1  # 字典进行初始化
            for key in xielv.keys():
                max_count = max(max_count, xielv[key] + 1)
            max_count = max(infinite, max_count)
        return max_count
    
    def maxPoints(self, points):
        max_count = 0 # 最多有多少个点在一条直线上
        for i in range(len(points)):
            initNode_x = points[i][0]
            initNode_y = points[i][1]
            heng = 0 # 因为求斜率分母不能为0，所以要单独计算平行于x轴的线段
            xielvs = {}  # 计算斜率相等，也就是以该起始点的一条直线上的的点数
            for j in range(i + 1, len(points)):
                dx = points[j][0] - initNode_x
                dy = points[j][1] - initNode_y
                if dx == 0:
                    heng += 1
                else:
                    xielv = dy // dx
                    if xielv not in xielvs:
                        xielvs[xielv] = 1
                    else:
                        xielvs[xielv] += 1
            for x in xielvs.values():
                max_count = max(max_count, x, heng)
        return max_count + 1 # 加上起始点
            
        

# 主函数
if __name__ == '__main__':
    point1 = Point(1, 2)
    point2 = Point(3, 6)
    point3 = Point(0, 0)
    point4 = Point(4, 7)
    points = [[point1.x, point1.y], [point2.x, point2.y], [point3.x, point3.y], [point4.x, point4.y]]
    print("初始点：", [[point1.x, point1.y], [point2.x, point2.y], [point3.x, point3.y], [point4.x, point4.y]])
    solution = Solution()
    print("结果：", solution.maxPoints(points))
