class Solution:
    def intersection(self, nums1, nums2):
        return set(nums1) & set(nums2)
if __name__ == '__main__':
    temp = Solution()
    List1 = [1,2,3,4]
    List2 = [2,4,6,8]
    print("输入："+str(List1)+"  "+str(List2))
    print(("输出："+str(temp.intersection(List1,List2))))