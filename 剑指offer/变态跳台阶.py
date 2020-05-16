class Solution:
    def jumpFloorII(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        else:
            SUM = [1, 2]
            for i in range(number - 2):
                temp = sum(SUM) + 1
                SUM.append(temp)
            return SUM

if __name__ == '__main__':
    solution = Solution()
    print(solution.jumpFloorII(4))