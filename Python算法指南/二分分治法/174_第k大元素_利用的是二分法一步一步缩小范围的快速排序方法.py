class Solution:
    def kthLargestElement(self, k, A):
        if not A or k < 1 or k > len(A):
            return None
        return self.partition(A, 0, len(A) - 1, len(A) - k)
    def partition(self, nums, start, end, k):
        if start == end:
            return nums[k]
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        # left is not bigger than right
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)
        return nums[k]
# 主函数
if __name__ == '__main__':
    A = [2, 3, 4, 1, 6, 5]
    k = 2
    print('初始数组和k值：', A, k)
    solution = Solution()
    print('第{}大元素是:'.format(k), solution.kthLargestElement(k, A))