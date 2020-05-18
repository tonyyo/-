class Solution:
    def woodCut(self, L, k):
        if not L:
            return 0
        start, end = 1, max(L)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_pieces(L, mid) >= k:
                start = mid
            else:
                end = mid
        return start

    def get_pieces(self, L, length):
        pieces = 0
        for l in L:
            pieces += l // length
        return pieces
if __name__ == '__main__':
    temp = Solution()
    L = [232, 124, 456]
    k = 7
    print("输入："+str(L))
    print("输入："+str(k))
    print("输出："+str(temp.woodCut(L,k)))