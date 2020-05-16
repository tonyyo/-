class Solution():
    def judgeZero(self, n):
        count = 0
        for i in range(5, n + 1):
            while i % 5 == 0: # 判断是否还有5
                count += 1
                i //= 5  # 去除5
        return count
if __name__ == '__main__':
    a = int(input("请输入："))
    solution = Solution()
    print(solution.judgeZero(a))