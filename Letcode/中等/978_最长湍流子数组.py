class Solution:
    def maxTurbulenceSize(self, A: [int]) -> int:
        N, maxLen = len(A), 1
        # up, down  = [0] * N, [0] * N
        # up[0], down[0] = 1, 1
        up, down = 1, 1
        for i in range(1, N):
            if A[i - 1] < A[i]:
                # up[i] = down[i-1] + 1
                # down[i] = 1
                up = down + 1
                down = 1
            elif A[i - 1] > A[i]:
                # down[i] = up[i-1] + 1
                # up[i] = 1
                down = up + 1
                up = 1
            else:
                # up[i] = 1
                # down[i] = 1
                up, down = 1, 1
            # maxLen = max(maxLen, up[i], down[i])
            maxLen = max(maxLen, up, down)
        return maxLen

if __name__ == '__main__':
    solution = Solution()
    A = [9,4,2,10,7,8,8,1,9]
    print(solution.maxTurbulenceSize(A))