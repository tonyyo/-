class Solution:
    def trapRainWater1(self, heights):
        if not heights:
            return 0
        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]
        water = 0
        while left <= right:
            if left_max < right_max:
                left_max = max(left_max, heights[left])
                water += left_max - heights[left]
                left += 1
            else:
                right_max = max(right_max, heights[right])
                water += right_max - heights[right]
                right -= 1
        return water

    def trapRainWater(self, heights):
        size = len(heights)
        left, right = 0, size - 1
        left_max, right_max = heights[left], heights[right]
        sum = 0
        while left <= right:
            if left_max < right_max:
                left_max = max(left_max, heights[left])
                sum += left_max - heights[left]
                left += 1
            else:
                right_max = max(right_max, heights[right])
                sum += right_max - heights[right]
                right -= 1
        return sum

if __name__ == '__main__':
    temp = Solution()
    List1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(("输入："+str(List1)))
    print(("输出："+str(temp.trapRainWater(List1))))