class Solution:
    def fibonacci(self, n):
        a = 0
        b = 1
        for i in range(n - 1):
            a, b = b, a + b # a存上一个的和，b存现有的和
        return a
if __name__ == '__main__':
    temp = Solution()
    nums1 = 5
    nums2 = 15
    print ("输入："+str(nums1))
    print ("输出："+str(temp.fibonacci(nums1)))
    print ("输入："+str(nums2))
    print ("输出："+str(temp.fibonacci(nums2)))