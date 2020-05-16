import collections


class Solution:
    def threeSumClosest(self, numbers, target):
        hash = [] # 这里不能用集合，因为集合不支持sorted。
        for i in range(len(numbers)):
            temp = abs(target - numbers[i])
            hash.append([temp, i])
        hash = sorted(hash, key=lambda x : x[0])
        SUM = 0
        for i in range(3):  # 如果求最接近的n个数之和，那么这里换成n就好了
            SUM += numbers[hash[i][1]]
        return SUM

if __name__ == '__main__':
    temp = Solution()
    List1 = [-1, 2, 1, -4]
    nums1 = 1
    print(("输入：" + str(List1) + "  " + str(nums1)))
    print(("输出：" + str(temp.threeSumClosest(List1, nums1))))

# class Solution:
#     def threeSumClosest(self, numbers, target):
#         numbers.sort()  # 其实就是要找到三个数的和离target最近的三个值, 所以先排序
#         ans = None
#         for i in range(len(numbers)):
#             left, right = i + 1, len(numbers) - 1
#             while left < right:
#                 sum = numbers[left] + numbers[right] + numbers[i]
#                 if ans is None or abs(sum - target) < abs(ans - target):
#                     ans = sum
#                 if sum <= target:   #这里用sum取代了mid, sum时left\right\num[i]的和, 但这里很明显存在着
#                     # 重复计算
#                     left += 1
#                 else:
#                     right -= 1
#         return ans
