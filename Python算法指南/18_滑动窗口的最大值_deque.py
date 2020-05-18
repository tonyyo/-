from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        queue = deque()
        ans = []
        for i in range(k):
            queue.append(nums[i])
        ans.append(max(queue))
        for i in range(k, len(nums)):
            queue.popleft()
            queue.append(nums[i])
            ans.append(max(queue))
        return ans

if __name__ == '__main__':
    solution = Solution()
    A = [2, 6, 5, 3, 1, 8]
    print(solution.maxSlidingWindow(A, 2))
