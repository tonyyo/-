class Solution:
    def isPerfectSquare2(self, n):
        if (int(n ** 0.5)) ** 2 == n:  # 判断该数是不是完全平方数
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution();
    print(solution.isPerfectSquare2(6))

# import math
# class 判断平方数:
#     def isPerfectSquare(self,n):
#         l = 0
#         r = n
#         while r > l:
#             mid = (l + r) // 2
#             if mid * mid <= n:
#                 if mid * mid == n:
#                     l = mid
#                     break
#                 l = mid
#             else:
#                 r = mid
#         ans = l
#         return ans * ans == n
#
#     def isPerfectSquare2(self, n): #根据Python的整除符号和除符号制定的专门解法
#         sq = math.sqrt(n)
#         return math.ceil(sq) == sq