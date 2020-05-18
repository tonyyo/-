class Solution:
    def maxEnvelopes1(self, envelopes):
        height = [a[1] for a in sorted(envelopes, key = lambda x: (x[0], -x[1]))]
        dp, length = [0] * len(height), 0
        import bisect
        for h in height:
            i = bisect.bisect_left(dp, h, 0, length)
            dp[i] = h
            if i == length:
                length += 1
        return length

    def maxEnvelopes(self, envelopes):
        envelopes = sorted(envelopes, key = lambda x : (x[0], x[1]))
        count = 1
        x, y = envelopes[0][0], envelopes[0][1]
        for i in range(1, len(envelopes)):
            if envelopes[i][0] > x and envelopes[i][1] > y:
                count += 1
                x, y = envelopes[i][0], envelopes[i][1]
        return count

if __name__ == '__main__':
    temp = Solution()
    List = [[5,4], [6, 4], [6, 7], [2, 3]]
    print(("输入："+str(List)))
    print(("输出："+str(temp.maxEnvelopes(List))))