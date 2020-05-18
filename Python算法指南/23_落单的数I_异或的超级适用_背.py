class Solution:
    def singleNumber(self, A):
        ans = 0
        for x in A:
            ans ^= x   # 一个数与0异或等于自身
        return ans

if __name__ == '__main__':
    solution = Solution()
    list1 = [4, 6, 4, 6, 3]
    list2 = [2, 1, 1, 1, 1]
    print(solution.singleNumber(list1))
    print(solution.singleNumber(list2))