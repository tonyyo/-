class Solution:
    def sqrt(self, n):
        l, r = 0, n
        while l + 1 < r:
            mid = (l + r) // 2
            if mid * mid < n:
                l = mid
            else:
                r = mid
        if r * r == n:
            return r
        else:
            return l


if __name__ == '__main__':
    solution = Solution()
    print(solution.sqrt(5))

# class Solution:
#     def sqrt(self, n):
#         l = 0
#         r = n
#         while l + 1 < r:   # 去3-4之间即可
#             mid = (l + r) // 2
#             if mid * mid <= n:
#                 if mid * mid == n:
#                     l = mid
#                     break
#                 l = mid
#             else:
#                 r = mid
#         return l