class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        length = len(heights)
        area = 0
        stack = []
        for i in range(length):
            while stack and heights[stack[-1]] > heights[i]:
                hight_index = stack.pop()
                hight = heights[hight_index]
                width = i - hight_index
                print(hight * width)
                area = max(area, width * hight)
            stack.append(i)
        return area

    def largestRectangleArea2(self, heights):
        heights.append(0) # 最后一个元素是最低的元素，那么就会弹出栈中所有的元素
        stack = []
        area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]: # 如果遇到了低的直方图，就要开始计算面积了
                high_index = stack.pop()  # 始终弹出最高的那个直方图的那个高
                high = heights[high_index]
                width = i - high_index   # 宽的话等于最高直方图索引和当前索引的差值
                print(width * high)
                area = max(area, width * high)
            stack.append(i) # 往stack加的永远是最高的那个元素
        return area


#主函数
if __name__=="__main__":
    heights=[2, 1, 5, 6, 2, 3]
    #创建对象
    solution=Solution()
    print("输入每个直方图的高度：",heights)
    print("找到的直方图的最大面积：",solution.largestRectangleArea(heights))
    print("找到的直方图的最大面积：",solution.largestRectangleArea2(heights))

# class Solution:
#     def largestRectangleArea(self, heights):
#         indices_stack = []
#         area = 0
#         for index, height in enumerate(heights + [0]):  # 将列表转化为索引序列, 包含索引
#             while indices_stack and heights[indices_stack[-1]] >= height:
#                 popped_index = indices_stack.pop()   # 遇到更小值的话, 弹出更大值
#                 left_index = indices_stack[-1] if indices_stack else -1  # 找到最左边元素的索引
#                 width = index - left_index - 1  # -1 是因为之前已经弹出来一个, 求面积是不断往前求最大面积.
#                 area = max(area, width * heights[popped_index])
#             indices_stack.append(index)
#         return area