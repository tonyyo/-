from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or not k:
            return []
        dq = deque()  # dq用来存储最大元素的索引坐标
        ans = []
        for i in range(k):
            dq.append(nums[i])
        ans.append(max(dq))
        for i in range(k, len(nums), 1):
            dq.popleft()
            dq.append(nums[i])
            ans.append(max(dq))
        return ans

if __name__ == '__main__':
    solution = Solution()
    A = [2, 6, 5, 3, 1, 8]
    print(solution.maxSlidingWindow(A, 2))

# class Solution:
#     def push(self, dq, nums, i):
#         while dq and nums[dq[-1]] < nums[i]: # 剔除比num[i] 小的末端元素
#             dq.pop()
#         dq.append(i)  #
#     def maxSlidingWindow(self, nums, k):
#         if not nums or not k:
#             return []
#         dq = deque()  # dq用来存储最大元素的索引坐标
#         for i in range(k - 1):
#             self.push(dq, nums, i)
#         result = []
#         for i in range(k - 1, len(nums)):
#             self.push(dq, nums, i)
#             result.append(nums[dq[0]])
#             if dq[0] == i - k + 1:
#                 dq.popleft()
#         return result
