class Solution:
    def fibonacci(self, n):
        a = 0
        b = 1
        for i in range(n - 1):
            a, b = b, a + b
        return a
if __name__ == '__main__':
    temp = Solution()
    nums1 = 5
    nums2 = 15
    print ("输入："+str(nums1))
    print ("输出："+str(temp.fibonacci(nums1)))
    print ("输入："+str(nums2))
    print ("输出："+str(temp.fibonacci(nums2)))