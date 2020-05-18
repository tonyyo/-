class Solution:
    def removeDuplicates(self, A):
        if A == []:
            return 0
        index = 0
        for i in range(1, len(A)):
            if A[i - 1] == A[i]:
                continue
            index += 1
        return index + 1

    def removeDuplicates2(self, nums):
        nums = set(nums)
        return len(nums)


if __name__ == '__main__':
    temp = Solution()
    List1 = [1, 2, 3, 3]
    List2 = [2, 5, 1, 3]
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.removeDuplicates(List1))))
    print(("输入：" + str(List2)))
    print(("输出：" + str(temp.removeDuplicates(List2))))
