class Solution():
    def countNag(self, List):
        count1, count2, Sum = 0, 0, 0
        for x in List:
            if x < 0:
                count1 += 1
            else:
                Sum += x
                count2 += 1
        avg = 0.0 if count2 == 0 else Sum / count2
        print(count1)
        print(round(avg, 1))
if __name__ == '__main__':
    solution = Solution()
    List = list()
    while True:
        try:
            List = list(map(int, input().strip().split()))
        except:
            break
    solution.countNag(List)

