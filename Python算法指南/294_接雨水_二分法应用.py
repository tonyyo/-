class Solution:
    def trap(self, heights):
        result, N = 0, len(heights)
        if N == 0:
            return 0
        left, right = 0, len(heights) - 1
        leftMax, rightMax = heights[0], heights[-1]
        while left <= right:
            if leftMax < rightMax:
                if leftMax < heights[left]:
                    leftMax = heights[left]
                else:
                    result += leftMax - heights[left]
                left += 1
            else:
                if rightMax < heights[right]:
                    rightMax = heights[right]
                else:
                    result += rightMax - heights[right]
                right -= 1
        return result


if __name__ == '__main__':
    temp = Solution()
    List1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(("输入："+str(List1)))
    print(("输出："+str(temp.trap(List1))))