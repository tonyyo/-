class Solution:
    def woodCut(self, L, k):
        ad_length = sum(L) // len(L)
        while True:
            count = 0
            for x in L:
                count += x // ad_length
            if count >= k: # 如果切分后的段数大于等于k，那么跳出循环
                break
            ad_length -= 1
        return ad_length


if __name__ == '__main__':
    temp = Solution()
    L = [232, 124, 456]
    k = 7
    print("输入："+str(L))
    print("输入："+str(k))
    print("输出："+str(temp.woodCut(L,k)))