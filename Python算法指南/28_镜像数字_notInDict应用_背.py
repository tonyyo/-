class Solution:
    def isStrobogrammatic(self, num):
        list1 = {"0" : '0',
                 "1" : '1',
                 "6" : '9',
                 "8" : '8',
                 "9" : '6'}
        for i in range(len(num)):
            if num[i] not in list1:
                return False
            if num[i] != list1[num[len(num) - i - 1]]:
                return False
        return True
if __name__ == '__main__':
    num = "986"
    solution = Solution()
    print(solution.isStrobogrammatic(num))