class Solution:
    def distributeCandies(self, candies: [int]) -> int:
        return len(set(candies)) if len(set(candies)) <= len(candies)//2 else len(candies) // 2
        # 种类数小于糖果的一半，表明有些糖果不止一个，那么妹妹每种糖果都可以有一个，所以是len(set(candies))
        # 种类数大于糖果的一半，表明有些糖果只有一个，那么为保证平均，妹妹最多只能获得len(candies)//2的糖果数，其中每个糖果的种类都不同