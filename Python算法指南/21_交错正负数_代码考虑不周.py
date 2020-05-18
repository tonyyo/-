class Solution:
    def subfun(self, A, B):
        ans = []
        for i in  range(len(B)):
            ans.append(A[i])
            ans.append(B[i])
        ans.append(A[-1])
        return ans

    def rerange(self, A):
        A1 = [i for i in A if i > 0 ]
        A2 = [i for i in A if i < 0 ]
        ans = []
        if len(A1) >= len(A2):
            ans = self.subfun(A1, A2)
        else:
            ans = self.subfun(A2, A1)
        return ans

if __name__ == '__main__':
    solution = Solution()
    A = [-1, -2, -3, 4, 5, 6, 7, 8]  #当正负数列表中有一个列表的长度大于另一个列表的长度值超过2时, 终将有元素被舍去.
    print(solution.rerange(A))
#
# class Solution:
#     def subfun(self, A, B):
#         ans = []
#         for i in range(len(B)):
#             ans.append(A[i])
#             ans.append(B[i])  # 因为A B为一正一负, 所以可以直接这么写
#         if (len(A) > len(B)):
#             ans.append((A[-1]))  # 如果A的长度比B长, 那么将A的最后一个元素放到最后,如果B的长度比A长 , 那就gg ,所以下面会判断
#         return ans
#
#     def rerange(self, A):
#         Ap = [i for i in A if i > 0]  #将A中所有的正数放到一个列表
#         Am = [i for i in A if i < 0]  #将A中所有的负数放到一个列表
#         tmp = []
#         if(len(Ap) > len(Am)):
#             tmp = self.subfun(Ap, Am)
#         else:
#             tmp = self.subfun(Am, Ap)
#         for i in range(len(tmp)):
#             A[i] = tmp[i]
#         return tmp