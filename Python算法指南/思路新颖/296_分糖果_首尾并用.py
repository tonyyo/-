class Solution:
    def candy(self, ratings):
        candynum = [1 for i in range(len(ratings))]  # 每个小孩至少有一个糖果
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candynum[i] = candynum[i - 1] + 1    # 如果右边的排名更高，在前者的基础上加一个糖果
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i + 1] < ratings[i] and candynum[i + 1] >= candynum[i]:
                candynum[i] = candynum[i + 1] + 1   # 如果左边的排名更高， 在后者的基础上加一个糖果
        return sum(candynum)

if __name__ == '__main__':
    temp = Solution()
    List1 = [2, 3, 1, 1, 4]
    List2 = [1, 4, 2, 2, 3]
    print(("输入：" + str(List1)))
    print(("输出：" + str(temp.candy(List1))))
    print(("输入：" + str(str(List2))))
    print(("输出：" + str(temp.candy(List2))))
