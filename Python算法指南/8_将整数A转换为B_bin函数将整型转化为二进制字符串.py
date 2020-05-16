import collections

class Solution:
    def bitSwapRequired(self, a, b):
        c = a ^ b
        cnt = 0
        for i in range(32):
            if c & (1 << i) != 0: #数1的个数的方法
                cnt += 1
        return cnt
    def bitSwapRequired2(self, a, b):
        a = int(bin(a)[2:])
        b = int(bin(b)[2:])   # bin函数返回的是字符串类型
        result = a ^ b
        string = str(result)
        list1 = list(string)  # 数字类型要转化为列表, 需要先转化为字符串
        c = collections.Counter(list1)  # Couoter返回的是字典类型, 键是字符串, 值是计数的数字
        return c["1"]
if __name__ == '__main__':
    solution = Solution()
    print(solution.bitSwapRequired2(31, 14))