import collections
class Solution:
    def singleNumberII(self, A):
        sum = [0] * 32
        for i in range(32):
            for x in A:
                if (x & (1 << i)) > 0:  # 与运算十进制会自动转化为二进制
                    sum[i] += 1
        ans = 0
        print(sum)
        for i in range(len(sum)):
            sum[i] = sum[i] % 3
            if sum[i] == 1:
                ans = ans + (1 << i)  # 加法运算二进制会自动转化为十进制
        return ans

if __name__ == '__main__':
    list1 = [4, 6, 4, 6, 3, 4, 6]
    solution = Solution()
    print(solution.singleNumberII(list1))