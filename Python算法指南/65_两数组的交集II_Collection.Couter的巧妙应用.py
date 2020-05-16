import collections


class Solution:
    def intersection(self, nums1, nums2):
        counts = collections.Counter(nums1)
        ans = []
        for x in nums2:
            if counts[x] > 0:  # 很巧, 这种以另一个数组中的元素为另一个数组中的索引的方法很巧
                ans.append(x)
                counts[x] -= 1
        return ans

if __name__ == '__main__':
    temp = Solution()
    List1 = [1, 2, 3, 4, 5, 6]
    List2 = [2, 4, 6, 8, 10]
    print(("输入：" + str(List1) + "  " + str(List2)))
    print(("输出：" + str(temp.intersection(List1, List2))))

# import collections
# class Solution:
#     def intersection(self, nums1, nums2):
#         counts = collections.Counter(nums1)
#         result = []
#         for num in nums2:
#             if counts[num] > 0:
#                 result.append(num)
#                 counts[num] -= 1
#         return result
