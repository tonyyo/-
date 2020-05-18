class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        result = self.grayCode(n - 1)
        print(result)
        seq = list(result)
        for i in reversed(result):
            seq.append((1 << (n - 1)) | i)
        return seq

#主函数
if __name__ == '__main__':
    n = int(input("请输入一个非负整数；"))
    solution = Solution()
    print("格雷编码的结果是：", solution.grayCode(n))