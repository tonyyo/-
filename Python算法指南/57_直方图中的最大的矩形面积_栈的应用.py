class Solution:
    def largestRectangleArea(self, heights):
        if len(heights) == 0:
            return 0
        heights.append(0)    # 末尾添加最低位， 使得最后所有栈中的元素都会出栈
        length = len(heights)
        area = 0
        stack = []
        for i in range(length):
            while stack and heights[stack[-1]] > heights[i]:  # 遇到低的就出栈
                hight_index = stack.pop()
                hight = heights[hight_index]
                left_index = stack[-1] if stack else -1       # 如果栈为0，那么宽度应该等于弹出位的坐标。
                width = i - left_index - 1   # 当栈不为空时，宽度等于当前低位坐标减出栈位坐标
                area = max(area, width * hight)
            stack.append(i)    # heights[i]存入栈中时一定是最高的
        return area
#主函数
if __name__=="__main__":
    heights=[2, 2, 3, 3, 5, 0]
    #创建对象
    solution=Solution()
    print("输入每个直方图的高度：",heights)
    print("找到的直方图的最大面积：",solution.largestRectangleArea(heights))

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