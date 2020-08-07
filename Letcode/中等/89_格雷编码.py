class Solution:
    def grayCode(self, n: int) -> [int]:
        res, vis = [0], [0]  # 题目中唯一要求从0开始，其余的顺序随便
        def dfs(cur): # 找到所有与cur二进制位唯一不同的数
            for i in range(n):
                nxt = cur ^ (1 << i) # 任何位与1异或得到相反数，与0异或得到本身
                if nxt in vis:
                    continue
                vis.append(nxt)
                res.append(nxt)
                dfs(nxt)
        dfs(0)
        return res