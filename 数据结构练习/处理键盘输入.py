class Solution():
    def print(self, List):
        for x in list:
            print(x)

if __name__ == '__main__':
    solution = Solution()
    n1, n2 = map(int, input("请输入两个数:").strip().split()) # 单行接收已知个参数

    # line = list(map(int, input("请输入一行：").strip().split()))  # 单行将一行数字存入列表

    # line = input("请输入一行：").strip().split() # 单行将一行字符串存入列表

    mx = []          #  存储二维列表
    for _ in range(n2):  # 假如n2是行数
        string = input().strip()
        lineList = list(map(int, string.split()))
        mx.append(lineList)
    print(mx)
