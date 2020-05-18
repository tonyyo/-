class Solution:
    def isHappy1(self, n):
        d = {}
        while True:
            m = 0
            while n > 0:
                m += (n % 10) ** 2  # 这是得到n的各位数字，直接进行平方
                n //= 10  # 是对n进行取整
            if m in d:
                return False
            if m == 1:
                return True
            d[m] = m  # 如果当前m不等于1，且在字典中不存在，则将其添加到字典中
            n = m

    def isHappy(self, n):
        result = []
        while n != 1:
            result.append(n)
            tempN = n
            n = 0
            while tempN != 0:
                g = tempN % 10
                tempN = tempN // 10
                n += g * g
            if n in result:
                return False
        return True
# 主函数
if __name__ == "__main__":
    n = 1
    # 创建对象
    solution = Solution()
    print("初始的数字是 ", n)
    print(" 最终结果是：", solution.isHappy(n))
