import collections


class Solution:
    def majorityNumber2(self, nums):
        key, count = None, 0
        for num in nums:
            if key is None:
                key, count = num, 1
            else:
                if key == num:
                    count += 1
                else:
                    count -= 1
            if count == 0:
                key = None
        return key

    def majorityNumber(self, nums):
        counts = collections.Counter(nums)
        size = len(nums)
        for key, val in counts.items():
            if counts[key] > size // 2:
                return key
        return -1

if __name__ == '__main__':
    temp = Solution()
    nums1 = [2, 2, 2, 3, 3, 3, 3]
    nums2 = [1, 2, 3, 4]
    print("输入的数组：" + "[2,2,2,3,3,3,3]" + "\n输出：" + str(temp.majorityNumber(nums1)))
    print("输入的数组：" + "[1,2,3,4]" + "\n输出：" + str(temp.majorityNumber(nums2)))
