class Solution:
    def maxArea(self, height: [int]) -> int:
        maxArea = 0
        N = len(height)
        left, right = 0, N - 1
        while left < right:
            high = min(height[left], height[right])
            di = right - left
            maxArea = max(maxArea, high * di)
            if height[left] == high:
                left += 1
            else:
                right -= 1
        return maxArea
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
