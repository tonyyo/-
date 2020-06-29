class Solution:
    def calPoints2(self, ops):
        # Time: O(n)
        # Space: O(n)
        history = []
        for op in ops:
            if op == 'C':
                history.pop()
            elif op == 'D':
                history.append(history[-1] * 2)
            elif op == '+':
                history.append(history[-1] + history[-2])
            else:
                history.append(int(op))
        return sum(history)

# 主函数
if __name__ == "__main__":
    ops = ["5", "2", "C", "D", "+"]
    # 创建对象
    solution = Solution()
    print("初始字符串数组是：", ops)
    print("总得分数是：", solution.calPoints(ops))
