class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints1(self, points):
        len_points = len(points)
        if len_points <= 1:
            return len_points
        max_count = 0
        for index1 in range(0, len_points):
            p1 = points[index1]
            gradients = {}
            infinite_count = 0
            duplicate_count = 0
            for index2 in range(index1, len_points):
                p2 = points[index2]
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                if 0 == dx and 0 == dy:
                    duplicate_count += 1  # 重复的点
                if 0 == dx:
                    infinite_count += 1  # 垂直于x轴的直线, 因为dx不能等于0
                else:
                    g = float(dy) / dx
                    gradients[g] = (gradients[g] + 1 if g in gradients else 1)
            if infinite_count > max_count:  # 如果该类线最大
                max_count = infinite_count
            print(gradients)
            for k, v in gradients.items():
                v += duplicate_count
                if v > max_count:
                    max_count = v
        return max_count

    def maxPoints(self, points):
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

# 主函数
if __name__ == '__main__':
    point1 = Point(1, 2)
    point2 = Point(3, 6)
    point3 = Point(0, 0)
    point4 = Point(4, 7)
    points = [point1, point2, point3, point4]
    print("初始点：", [[point1.x, point1.y], [point2.x, point2.y], [point3.x, point3.y], [point4.x, point4.y]])
    solution = Solution()
    print("结果：", solution.maxPoints(points))
