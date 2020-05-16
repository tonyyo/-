class Solution:
    def countOnes(self, num):
        total = 0
        for i in range(32):
            total += num & 1
            num >>= 1
        return total
if __name__ == '__main__':
    temp = Solution()
    nums1 = 32
    nums2 = 15
    print(("输入："+str(nums1)))
    print(("输出："+str(temp.countOnes(nums1))))
    print(("输入："+str(nums2)))
    print(("输出："+str(temp.countOnes(nums2))))