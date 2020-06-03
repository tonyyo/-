class Solution():
    def hanmingWeight(self, a):
        count = 0
        for i in range(32):
            if ((1 << i) & a ) != 0:  # 最好将1向左移动，而不是将数向右移动，因为算术右移的话，左侧补的是符号位
                count += 1
        return count
if __name__ == '__main__':
    solution = Solution()
    print(solution.hanmingWeight(-1))