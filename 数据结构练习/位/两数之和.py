class Solution():
    def TwoSum(self, a, b):
        while b != 0:
            temp = a ^ b  # 无进位加法， 包含原始位相加， 也包含进位之间相加
            b = (a & b) << 1  # 计算进位，当不存在进位时， 自然也就不需要了无进位加法
            a = temp  # 下一轮要进行无进位加法的a
        return a
if __name__ == '__main__':
    solution = Solution()
    print(solution.TwoSum(14,12))