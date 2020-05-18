class Solution:
    def checkPowerOf2(self, n):
        while n % 2 == 0: # 如果有2的因子, 那么结果就会是0
            n = n // 2
        if n == 1:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.checkPowerOf2(352))

    import math
    #
    #
    # class Solution:
    #     def checkPowerOf2(self, n):
    #         i = 0
    #         while i < n:
    #             if math.pow(2, i) == n:
    #                 return 1
    #             i = i + 1
    #         else:
    #             return 0