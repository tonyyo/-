class Solution():
    def strSplit(self, List):
        for x in List:
            l = len(x)
            y = l % 8
            for i in range(0, l - y, 8):
                print(x[i : i + 8])
            if y != 0:
                print(x[l - y:] + '0' * (8 - y))

if __name__ == '__main__':
    solution = Solution()
    while True:
        try:
            N = int(input())
            List = list()
            for _ in range(N):
                List.append(input())
            solution.strSplit(List)
        except:
            break

