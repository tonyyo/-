class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        m, n = len(nums1), len(nums2)
        k = (m + n) // 2
        if (m + n) & 1 == 1:
            return self.findKth(nums1, nums2, k + 1)  # 5 // 2 = 2
        else:
            return (self.findKth(nums1, nums2, k) + self.findKth(nums1, nums2, k + 1)) / 2

    def findKth(self, nums1, nums2, k):  # 找第k小的数
        if len(nums1) < len(nums2):  # 始终保持nums1更长
            nums1, nums2 = nums2, nums1
        if len(nums2) == 0:
            return nums1[k - 1]  # 找到第k小的数，所以这里应该是k - 1
        if k == 1:
            return min(nums1[0], nums2[0])  # 找到第1小的数， 所以应该找二者第一个数的最小值
        i = min(k // 2, len(nums2))  # 每次去除的元素并不一定是k/2， 超过了nums2的长度， 只需去除nums2的长度即可
        if nums1[i - 1] < nums2[i - 1]:
            return self.findKth(nums1[i:], nums2, k - i)  # 舍去小的那一半
        else:
            return self.findKth(nums1, nums2[i:], k - i)
