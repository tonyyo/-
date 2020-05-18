class Solution:
    def sortColors2(self, colors):
        self.sort2(colors, 0, len(colors) - 1)

    def sort(self, colors, color_from, color_to):
        if color_from == color_to:
            return
        color = (color_from + color_to) // 2
        left, right = color_from, color_to
        while left <= right:
            while left <= right and colors[left] <= color:
                left += 1
            while left <= right and colors[right] > color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        self.sort(colors, color_from, color)
        self.sort(colors, color + 1, color_to)

    def sort2(self, colors, left, right):
        if left == right:
            return
        start, end = left, right
        mid = (start + end) // 2
        pivot = colors[mid]
        while start <= end:
            while start <= end and colors[start] <= pivot:
                start += 1
            while start <= end and colors[end] > pivot:
                end -= 1
            if start <= end:
                colors[start], colors[end] = colors[end], colors[start]
                start += 1
                end -= 1
        self.sort(colors, left, start)
        self.sort(colors, end, right)

# 主函数
if __name__ == '__main__':
    colors = [3, 2, 2, 1, 4, 5, 5, 6, 7]
    k = 4
    print("初始对象和颜色种类：", colors, k)
    solution = Solution()
    solution.sortColors2(colors)
    print("结果：", colors)
