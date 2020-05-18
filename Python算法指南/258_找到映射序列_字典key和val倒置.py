class Solution:
    def anagramMappings(self, A, B):
        mapping = {v: k for k, v in enumerate(B)}  # 因为可能重复, k取后面的
        return [mapping[value] for value in A]
#主函数
if __name__ == "__main__":
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
    #创建对象
    solution = Solution()
    print("输入的两个列表是A= ", A, "B=", B)
    print("输出的结果是：", solution.anagramMappings(A, B))