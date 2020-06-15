class Solution:
    def maxTurbulenceSize(self, A: [int]) -> int:
        asc, dsc = 1, 1
        maxLen = 1
        N = len(A)
        if N == 0:
            return 0
        for i in range(1, N):
            if A[i] > A[i - 1]:
                asc = dsc + 1
                dsc = 1
            elif A[i] < A[i - 1]:
                dsc = asc + 1
                asc = 1
            else:
                dsc = 1
                asc = 1
            maxLen = max(maxLen, asc, dsc)
        return maxLen


    def maxTurbulenceSize1(self, A: [int]) -> int:
        N = len(A)
        flag = 1  # flag 为1表示是上升趋势， 为0表示为下降趋势
        # dp = []  # dp[i]表示以第i个元素结尾的最长湍流子数组
        tmp = 1
        maxLen = 1
        for i in range(1, N):
            if A[i] - A[i - 1] < 0 and flag == 1:
                tmp += 1
                flag = 0
            elif A[i] - A[i - 1] > 0 and flag == 0:
                tmp += 1
                flag = 1
            elif A[i] == A[i - 1]:
                tmp = 1
            else:
                tmp = 2
            maxLen = max(maxLen, tmp)
        return maxLen

if __name__ == '__main__':
    solution = Solution()
    A = [9,4,2,10,7,8,8,1,9]
    print(solution.maxTurbulenceSize(A))
    print(solution.maxTurbulenceSize1(A))