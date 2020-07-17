class Solution:
    def isStraight(self, nums: [int]) -> bool:
        Max, Min = 0, 14
        already = []
        for x in nums:
            if x == 0:
                continue
            if x in already: # 除大王外不能重复
                return False
            already.append(x)
            Max = max(Max, x)
            Min = min(Min, x)
        return Max - Min < 5  # 五张牌中最大值和最小值之差小于5

if __name__ == '__main__':
    solution = Solution()
    print(solution.isStraight([0,0,8,5,4]))