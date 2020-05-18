class Solution(object):
    def maxArea1(self, height):
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left += 1
            else:
                area = height[right] * (right - left)
                right -= 1
            ans = max(ans, area)
        return ans

    def maxArea2(self, height):
        size = len(height)
        left, right = 0, size - 1
        max_area = 0
        while left + 1 <= right:
            area = 0
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left += 1
            else:
                area = height[right] * (right - left)
                right -= 1
            max_area = max(max_area, area)
        return max_area

    def maxArea(self, height):
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            if height[left] <= height[right]:
                area = max(area, height[left] * (right - left))
                left += 1
            else:
                area = max(area, height[right] * (right - left))
                right -= 1
        return area

if __name__ == '__main__':
    temp = Solution()
    List1 = [1, 2, 3]
    List2 = [2, 5, 1, 3]
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.maxArea(List1))))
    print(("输入：" + str(List2)))
    print(("输出：" + str(temp.maxArea(List2))))
