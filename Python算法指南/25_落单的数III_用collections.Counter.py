class Solution:
    def singleNumberIII(self, A):
        s = 0
        for x in A:
            s ^= x
        y = s & -s  # 这里的-s是补码, 因为计算机不认识负数, 只认识补码, 用补码表示负数
        ans = [0, 0]
        for x in A:
            if (x & y) != 0:  # 两数异或的结果与其补码相与, 可得到其中一个数的值
                ans[0] ^= x
            else:
                ans[1] ^= x
        return ans
if __name__ == '__main__':
    solution = Solution()
    list1 = [2, 2, 2, 3, 3, 1, 1, 1, 4, 4]
    print(solution.singleNumberIII(list1))
