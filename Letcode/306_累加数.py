class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        result = []

        def dfs(left_num, path):
            if len(path) > 2 and len(left_num) == 0:  # 数字被用完
                result.append(path)
                return
            for i in range(1, len(left_num) + 1):  # 遍历和的长度
                if i != 1 and left_num[0] == '0':  # 多位数字不能以0开头
                    return
                prefix = int(left_num[:i])
                if len(path) < 2 or prefix == path[-1] + path[-2]:  # 路径长度小于2或者满足条件时继续回溯
                    dfs(left_num[i:], path + [prefix])

        dfs(num, [])
        return bool(result)  # 有一条路径满足即可
if __name__ == '__main__':
    s = Solution()
    print(s.isAdditiveNumber("1023"))