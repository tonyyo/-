class Solution():
    def nextSparseNum(self, num):
        while not self.isSparseNum(num):
            num += 1
        return num

    def isSparseNum(self, num):
        strNum = bin(num)[2:]
        for i in range(1, len(strNum)):
            if strNum[i] != '1':
                continue
            else:
                if strNum[i - 1] == strNum[i]:
                    return False
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.nextSparseNum(6))