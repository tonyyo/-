class Solution():
    def ifPowOfTwo(self, a):
        return a > 0 and a & (a - 1) == 0 # 16 = 10000  and 15 = 01111
if __name__ == '__main__':
    solution = Solution()
    print(solution.ifPowOfTwo(14))