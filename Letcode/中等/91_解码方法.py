class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        if N == 0 or s[0] == '0' or s.find('00') != -1:  # 首字母为0时返回0, 含‘00’
            return 0
        if N == 1:
            return 1
        if s[1] == '0' and int(s[0]) > 2:    # '301'
            return 0
        if N == 2:
            return 2 if 0 < int(s[0:2]) <= 26 and s[0] != '0' and s[1] != '0' else 1
        a, b = 1, 2 if 0 < int(s[0:2]) <= 26 and s[0] != '0' and s[1] != '0' else 1
        for i in range(2, N):
            if int(s[i - 1 : i + 1]) <= 26:
                if s[i - 1] != '0' and s[i] != '0':  # 两位时不能大于26且其中不能有0
                    a, b = b, a + b
                if s[i - 1] != '0' and s[i] == '0':  # 当前为0时，只能走两步
                    a, b = b, a
                if s[i - 1] == '0' and s[i] != '0':  # 前一个为0时，只能走一步
                    a, b = b, b
            else:
                if s[i] == '0' and int(s[i - 1]) > 2:  # '230'
                    return 0
                else:
                    a, b = b, b   # 大于26时只能走一步
        return b
if __name__ == '__main__':
    solution = Solution()
    print(solution.numDecodings("30"))