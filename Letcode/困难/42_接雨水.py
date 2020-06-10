class Solution:
    def trap(self, height: [int]) -> int:
        N = len(height)
        if N == 0:
            return 0
        leftMax, rightMax = height[0], height[N-1]
        left, right, sum  = 1, N - 2, 0  # 双指针
        while left <= right:
            if leftMax < rightMax:
                if height[left] < leftMax:
                    sum += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if height[right] < rightMax:
                    sum += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1
        return sum
