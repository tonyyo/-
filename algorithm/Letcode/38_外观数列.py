class Solution(object):
    def countAndSay(self, n):
        char = '1'
        for i in range(n - 1):
            tempchar = ''   
            tempN = 1
            for j in range(len(char)):
                if j + 1 < len(char) and char[j] == char[j + 1]:
                    tempN += 1
                else:
                    tempchar += str(tempN) + char[j]
                    tempN = 1
            char = tempchar
        return char

if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(4))