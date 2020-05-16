class Solution:
    def candy(self, ratings):
        candynum = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candynum[i] = candynum[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i + 1] < ratings[i] and candynum[i + 1] >= candynum[i]:
                candynum[i] = candynum[i + 1] + 1
        return sum(candynum)

    def candy1(self, ratings):
        candy = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                candy[i] = candy[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i + 1] < ratings[i] and candy[i + 1] > candy[i]:
                candy[i] = candy[i + 1] + 1
        return sum(candy)

if __name__ == '__main__':
    temp = Solution()
    List1 = [2, 3, 1, 1, 4]
    List2 = [1, 4, 2, 2, 3]
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.candy1(List1))))
    print(("输入：" + str(str(List2))))
    print(("输出：" + str(temp.candy1(List2))))
