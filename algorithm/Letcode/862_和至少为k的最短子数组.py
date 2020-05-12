class Solution(object):
    #todo 官方的解法
    def shortestSubarray(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        #Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = collections.deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1

    #todo 尝试着用动态规划去做，思路不错，但是超时了
    def shortestSubarray0(self, A, K):
        N = len(A)
        f = [50001] * N  # f[i] 表示到A[i]位置时，和大于等于k的最小子数组长度
        for i in range(N):
            if i == 0:
                if A[i] >= K:
                    return 1
                else:
                    f[i] = -1
                continue
            sum, preMinLen = 0, f[i - 1]
            if preMinLen == -1:  # 1、前面没有和大于等于k的子数组的情况
                for j in range(i, -1, -1): # 前面没有和大于等于k的，那么带上A[i]后，看是否有等于k的
                   sum += A[j]
                   if sum >=K:
                        f[i] =i - j + 1
                        break
                if sum < K:
                    f[i] = -1
            else:  # 2、前面有和大于等于k的子数组的情况
                for j in range(preMinLen - 1):  # 带上A[i]之后，看是否有长度小于f[i-1]的
                    sum += A[i - j]
                    if sum >= K:
                        f[i] = j + 1
                        break
                if sum < K:
                    f[i] = preMinLen
        return f[N - 1]
if __name__ == '__main__':
    A = [77,19,35,10,-14]
    K = 19
    solution = Solution()
    print(solution.shortestSubarray(A, K))
