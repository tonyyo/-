# print(bin((1<<4) - 1))
# print((bin(((1 << 32) - 1) & -15)[2:]))  # 你用一个全1的数与负数相与，那么得到的就是它的补码，因为计算机里面存的就是补码。
# print(type(bin(((1 << 32) - 1) & -15)[2:]))  # bin函数返回的是字符串。
class Solution:
    def NumberOf1(self, n):
        return sum((n >> i & 1) for i in range(0,32))  # 利用的是计算机里存的本来就是补码