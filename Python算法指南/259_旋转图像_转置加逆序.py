class Solution:
    def rotate1(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix

    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):   # 只能交换一次
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # 因为是方阵,所以可以这样做
        for i in range(len(matrix)):
            matrix[i].reverse()
        return matrix

#主函数
if __name__ == "__main__":
    arr = [[1, 2], [3, 4]]
    #创建对象
    solution = Solution()
    print("输入的数组是：", arr)
    print("旋转后的矩阵是：", solution.rotate(arr))