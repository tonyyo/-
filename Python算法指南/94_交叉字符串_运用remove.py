class Solution:
    def isInterleave2(self, s1, s2, s3):
        if s1 is None or s2 is None or s3 is None:
            return False
        if len(s1) + len(s2) != len(s3):
            return False
        interleave = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        interleave[0][0] = True
        for i in range(len(s1)):
            interleave[i + 1][0] = s1[:i + 1] == s3[:i + 1]
        for i in range(len(s2)):
            interleave[0][i + 1] = s2[:i + 1] == s3[:i + 1]
        for i in range(len(s1)):
            for j in range(len(s2)):
                interleave[i + 1][j + 1] = False
                if s1[i] == s3[i + j + 1]:
                    interleave[i + 1][j + 1] = interleave[i][j + 1]
                if s2[j] == s3[i + j + 1]:
                    interleave[i + 1][j + 1] |= interleave[i + 1][j]
        return interleave[len(s1)][len(s2)]

    def isInterleave(self, s1, s2, s3):
        listS1 = list(s1)
        listS2 = list(s2)
        listS3 = list(s3)
        for x in listS1:
            listS3.remove(x)
        listS2.sort()
        listS3.sort()
        return listS3 == listS2

if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print("数组s1：", s1)
    print("数组s2：", s2)
    print("数组s3：", s3)
    solution = Solution()
    print("数组是否交叉：", solution.isInterleave(s1, s2, s3))