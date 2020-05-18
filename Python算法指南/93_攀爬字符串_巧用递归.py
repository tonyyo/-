class Solution:
    def isScramble2(self, s1, s2):
        if len(s1) != len(s2): return False
        if s1 == s2: return True  # 出口
        l1 = list(s1);
        l2 = list(s2)
        l1.sort();
        l2.sort()
        if l1 != l2: return False
        length = len(s1)
        for i in range(1, length):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]): return True
            if self.isScramble(s1[:i], s2[length - i:]) and self.isScramble(s1[i:], s2[:length - i]): return True
        return False

    def isScramble(self, s1, s2):
        size1 = len(s1)
        size2 = len(s2)
        tempS1 = sorted(s1)
        tempS2 = sorted(s2)
        if s1 == s2:
            return True
        if size1 != size2 and tempS1 != tempS2:
            return False
        for i in range(1, size1):  # 需从1开始, 不然无法截取字符串
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[size2 - i:]) and self.isScramble(s1[size2 - i:], s2[:i]):
                return True


if __name__ == '__main__':
    s1, s2 = "great", "rgeat"
    print("字符串s1：", s1)
    print("字符串s2：", s2)
    solution = Solution()
    print("s2 是否为 s1 的攀爬字符串：", solution.isScramble(s1, s2))
