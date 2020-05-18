class Solution:
    def addDigits(self, num):
        sum = 0
        while sum not in [1,2,3,4,5,6,7,8,9]:
            sum += num % 10
            num //= 10
            if num // 10 == 0:
                sum += num % 10
                if sum not in [1,2,3,4,5,6,7,8,9]:
                    num = sum
                    sum = 0
                else:
                    break
        return sum

    def addDigits2(self, num):
        list1 = list(str(num))
        list2 = list(map(int, list1))  # 这里的list类型转换不能少
        SUM = sum(list2)
        if len(str(SUM)) == 1:
            return SUM
        else:
            SUM = self.addDigits(SUM)
        return SUM

# 主函数
if __name__ == '__main__':
    num = 38
    print("初始值：", num)
    solution = Solution()
    print("结果：", solution.addDigits2(num))

