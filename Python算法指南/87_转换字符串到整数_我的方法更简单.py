import sys


class Solution(object):
    def atoi2(self, str):
        str = str.strip()  # 去除首尾空格
        if str == "":
            return 0
        i = 0
        sign = 1
        ret = 0
        length = len(str)
        MaxInt = (1 << 31) - 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            sign = -1
        for i in range(i, length):
            if str[i] < '0' or str[i] > '9':
                break
            ret = ret * 10 + int(str[i])
            if ret > sys.maxsize:
                break
        ret *= sign
        if ret >= MaxInt:
            return MaxInt
        if ret < MaxInt * -1:
            return MaxInt * - 1 - 1
        return ret

    def atoi(self, str):
        length = len(str)
        IntList = list(map(int, str))
        IntList.reverse()
        print(IntList)
        sum = 0
        for i in range(length):
            sum += IntList[i] * pow(10, i)
        return sum

if __name__ == '__main__':
    temp = Solution()
    string1 = "150"
    string2 = "32"
    print(("输入：" + string1))
    print(("输出：" + str(temp.atoi(string1))))
    print(("输入：" + string2))
    print(("输出：" + str(temp.atoi(string2))))
