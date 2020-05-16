class Solution:
    def countOfSmallerNumberII(self, A):
        ans = [0]
        for i in range(1, len(A)):
            count = 0
            for j in range(0, i, 1):
                if A[j] < A[i]:
                    count += 1
            ans.append(count)
        return ans
if __name__ == '__main__':
    temp = Solution()
    nums = [1, 2, 7, 8, 5]
    print(("输入：" + str(nums)))
    print(("输出：" + str(temp.countOfSmallerNumberII(nums))))
