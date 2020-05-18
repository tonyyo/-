class Solution(object):
    def mirror(self, Str):
        N = len(Str)
        mid = (N - 1) // 2
        if N % 2 == 0:
            return Str[:mid + 1] + Str[mid::-1]
        else:
            return Str[:mid + 1] + Str[mid - 1::-1]

    def get_small(self, Str):
        if int(self.mirror(Str)) < int(Str):  # 镜像回文串小于原数，就是小回文串
            return self.mirror(Str)
        N = len(Str)
        mid = (N - 1) // 2
        if 10 < int(Str) < 20:  # todo 待优化
            if int(Str) == 11:
                return "9"
            else:
                return "11"
        if N % 2 == 0:
            LeftHalf = str(int(Str[:mid + 1]) - 1)
            return LeftHalf + LeftHalf[::-1]
        else:
            templen = len(Str[:mid + 1])
            LeftHalf = str(int(Str[:mid + 1]) - 1)
            if len(LeftHalf) < templen:   # 10001  todo 待优化
                return LeftHalf + LeftHalf[::-1]
            else:
                return LeftHalf + LeftHalf[-2::-1]

    def get_big(self, Str):
        if int(self.mirror(Str)) > int(Str):
            return self.mirror(Str)
        N = len(Str)
        mid = (N - 1) // 2
        if N % 2 == 0:
            LeftHalf = str(int(Str[:mid + 1]) + 1)
            return LeftHalf + LeftHalf[::-1]
        else:
            LeftHalf = str(int(Str[:mid + 1]) + 1)
            return LeftHalf + LeftHalf[-2::-1]

    def nearestPalindromic(self, Str):
        if len(Str) == 1:
            if int(Str) == 0:
                return "1"
            else:
                return str(int(Str) - 1)
        if len(str(int(Str) - 1)) < len(Str): # 10 100 1000
            return str(int(Str) - 1)
        if len(str(int(Str) + 1)) > len(Str): # 99 999 99999  todo 待优化
            return str(int(Str) + 2)
        small = self.get_small(Str)
        big = self.get_big(Str)
        return big if int(big) - int(Str) < int(Str) - int(small) else small

    #todo 我的错误解法
    # 总结别人的解法：其实就是找到大于小于原数的两个大小回文串，看离原树的距离谁更近，就是最接近的。
    # 将回文串前半部分镜像，得到的回文串，如果大于原数，那么就是最近的大回文串，反之就是最近的的小回文串，
    # 如果相等，说明原数本身就是回文串，那么将前半部分加1减1再镜像就得到大小回文串，值得注意的是当为原数为奇数位时需讨论加减1会减少的情况；
    # 其中存在着四种特殊情况：
    # 1、当原数是个位数时，根据题意，最接近回文串等于原数直接减1就好
    # 2、当原数是个位数，且等于0时，最小回文串为"1”
    # 3、当原数是10的非0正整数倍时，最近回文串等于原数减1
    # 4、 当原数全为9时
    def nearestPalindromic0(self, n):
        strn = str(n)
        if len(strn) == 1 or int(n) == 10:
            return str(int(n) - 1)
        list1 = list(map(int, strn))
        mid = (len(list1) - 1) // 2
        #todo 解法错误，不是回文数的时候不是简单的将右边的替换为左边，例如19的最接近的数为22，而不是11
        if list1 != list1[::-1]:   # 1、不是回文数，只需将右边的数替换为左边的数即可
            if len(list1) % 2 == 0: # 偶数位
                list1[mid + 1:] = list1[mid::-1]
            else:
                list1[mid + 1:] = list1[mid - 1::-1]
        else:                      # 2、是回文数,需要更改中间值
            if len(list1) % 2 == 1:
                if list1[mid + 1] >= 5 and list1[mid] != 9 or list1[mid] == 0:
                    list1[mid] = list1[mid] + 1
                else:
                    list1[mid] = list1[mid] - 1
            else:
                if list1[mid + 2] >= 5 and list1[mid] != 9 or list1[mid] == 0:
                    list1[mid] = list1[mid] + 1
                    list1[mid + 1] = list1[mid + 1] + 1
                else:
                    list1[mid] = list1[mid] - 1
                    list1[mid + 1] = list1[mid + 1] - 1
        s = "".join(str(x) for x in list1)
        return s
if __name__ == '__main__':
    solution = Solution()
    print(solution.nearestPalindromic("10001"))




