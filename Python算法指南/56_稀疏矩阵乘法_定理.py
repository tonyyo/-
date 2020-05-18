class Solution:
    def multiply(self, A, B):
        rowNumA, colNumA = len(A), len(A[0])
        rowNumB, colNumB = len(B), len(B[0])
        res = [ [0] * colNumB for _ in range(rowNumA)]
        for i in range(rowNumA):
            for j in range(colNumB):
                for k in range(colNumA):
                    res[i][j] += A[i][k] * B[k][j]
        return res
# 主函数
if __name__ == "__main__":
    A = [[1, 0, 0], [-1, 0, 3]]
    B = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]  # 创建对象
    solution = Solution()
    print("输入的两个数组是A=", A, "B=", B)
    print("输出的结果是：", solution.multiply(A, B))

# class Solution:
#     def multiply(self, A, B):
#         n = len(A) # A的行数
#         m = len(A[0]) # A的列数
#         k = len(B[0]) # B的列数
#         C = [[0 for _ in range(k)] for i in range(n)] # 新矩阵以A的行为行, B的列为列
#         for i in range(n):
#             for j in range(m): # A的列数 等于 B的行数
#                 if A[i][j] != 0:
#                     for l in range(k):
#                         C[i][l] += A[i][j] * B[j][l]
#         return C