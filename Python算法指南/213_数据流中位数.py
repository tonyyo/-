import heapq
class Solution:
    def medianII(self, nums):
        self.minheap, self.maxheap = [], []
        medians = []
        for num in nums:
            self.add(num)
            medians.append(self.median)
        return medians
    @property
    def median(self):
        return -self.maxheap[0]
    def add(self, value):
        if len(self.maxheap) <= len(self.minheap):
            heapq.heappush(self.maxheap, -value)
        else:
            heapq.heappush(self.minheap, value)
        if len(self.minheap) == 0 or len(self.maxheap) == 0:
            return
        if -self.maxheap[0] > self.minheap[0]:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def medianII(self, nums):
        size = len(nums)
        ans = []
        for i in range(1,size + 1):
            tempList = sorted(nums[:i])
            ans.append(tempList[(len(tempList) - 1) // 2])
        return ans


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [4, 5, 1, 3, 2, 6, 0]
    nums3 = [2, 20, 100]
    solution = Solution()
    print("持续进入数组的列表是：", nums1)
    print("新数组的中位数是：", solution.medianII(nums1))
    print("持续进入数组的列表是：", nums2)
    print("新数组的中位数是：", solution.medianII(nums2))
    print("持续进入数组的列表是：", nums3)
    print("新数组的中位数是：", solution.medianII(nums3))