import collections


class Solution(object):
    #todo 官方的解法
    def shortestSubarray(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)   # 记录前n项和
        ans = N+1
        monoq = collections.deque()
        for y, Py in enumerate(P):
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()
            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())
            monoq.append(y)

        return ans if ans < N+1 else -1

    #todo 理解官方的解法，很奇妙，思路是乱序排队从前往后变为升序排队，将不按要求排队的人剔除，也就是高个子，这个时候算高度差，求出大于k的最短连续队列长度
    def shortestSubarray1(self, A, K):
        N = len(A)
        p = [0]  # 假设一个最矮的人的身高为0
        ans = N + 1
        for x in A:
            p.append(p[-1] + x)  # p表示一群不按升序站队的人的身高
        queue = collections.deque()  # 队列，存储着每个人站的位置
        for pos, height in enumerate(p):
            while queue and p[queue[-1]] >= height: # 队列里有人，当前队列里有人比要进入队列的人高，就踢出去,因为后面的人要尽量找最大高度差，高的人没用
                queue.pop()
            while queue and height - p[queue[0]] >= K: # 找到高度差大于等于k的， 知道完全比完，得到最小的
                ans = min(ans, pos - queue.popleft())
            queue.append(pos) # 重新站队咯
        return ans if ans != N + 1 else -1   # 没找到连续队列的高度差大于等于k的 返回-1

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
    A = [84,-37,32,40,95]
    K = 167
    solution = Solution()
    print(solution.shortestSubarray1(A, K))
    print(solution.shortestSubarray(A, K))
