import collections


class Solution:
    def findPairs(self, nums, k):
        if k == 0:
            return sum(x == 2 for x in collections.Counter(nums).values())
        if k > 0:
            list1 = list(set(nums) & set(x + k for x in nums))
            ans = []
            for x in list1:
                ans.append([x - 2, x])
            return ans

if __name__ == '__main__':
    temp = Solution()
    List1 = [6,3,4,2,5,1,1]
    num = 2
    print(("输入："+str(List1)+"  "+str(num)))
    print(("输出："+str(temp.findPairs(List1,num))))

# class Solution:
#     def findPairs(self, nums, k):
#         if k > 0:
#             return len(set(nums) & set(n + k for n in nums))
#         if k == 0: #计数所有出现的数字> 1
#             return sum(v > 1 for v in collections.Counter(nums).values())
#         return 0