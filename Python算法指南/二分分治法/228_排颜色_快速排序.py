class Solution:
    def sort2(self, colors, color_from, color_to):
        left, right = color_from, color_to
        if left >= right:
            return
        pivot = colors[left]
        while left < right:
            while left < right and colors[right] > pivot: # 在右边找大于等于哨兵的值放到左边
                right -= 1
            while left < right and colors[left] <= pivot: # 在左边找大于哨兵的值放到右边
                left += 1
            if left < right:
                colors[left], colors[right] = colors[right], colors[left]
        colors[left], colors[color_from] = colors[color_from], colors[left] # 将哨兵交换到中间
        self.sort2(colors, color_from, left - 1)
        self.sort2(color_from, left + 1, color_to)

# 主函数
if __name__ == '__main__':
    colors = [3, 2, 2, 1, 4, 5, 5, 6, 7]
    k = 4
    print("初始对象和颜色种类：", colors, k)
    solution = Solution()
    solution.sort2(colors, 0, len(colors) - 1)
    print("结果：", colors)
