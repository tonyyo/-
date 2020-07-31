from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # 从第m个开始, 之后k个中, 最大为第几个
        def find(m, k, nums):
            res = m
            for i in range(m + 1, m + k):
                if nums[i] > nums[res]:
                    res = i
            # print(m, m+k-1, res)
            return res

        # 初始从前k个找到最大的位置
        m = find(0, k, nums)
        res = [nums[m]]

        # 之后每次加入一个新的数
        for i in range(k, len(nums)):
            # 如果最大的从滑块左侧溢出, 找一个新的最大
            if i - k + 1 > m:
                m = find(i - k + 1, k, nums)
            # 否则与新加入的进行比较, 更新
            elif nums[m] < nums[i]:
                # print(m)
                m = i
            res.append(nums[m])


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))