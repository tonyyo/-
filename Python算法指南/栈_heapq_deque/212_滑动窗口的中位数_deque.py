import collections


class Solution:
    def medianSlidingWindow(self, nums, k):
        size = len(nums)
        ans = []
        queue = collections.deque()
        for i in range(k):
            queue.append(nums[i])
        ans.append(sorted(queue)[k // 2])
        for i in range(k, size):
            queue.popleft()
            queue.append(nums[i])
            ans.append(sorted(queue)[k // 2])
        return ans

if __name__ == '__main__':
    A = [1, 2, 7, 8, 5]
    print("输入的数组是：", A)
    solution = Solution()
    print("滑动窗口的中位数是：", solution.medianSlidingWindow(A, 3))