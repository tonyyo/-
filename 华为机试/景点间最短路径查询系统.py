class Solution():
    def minLen(self, mx, n, q):
        NameByNo = dict()
        chedaoByName = dict()
        N = len(mx)
        for i in range(2 * n - 2):
            key = mx[i][0] + mx[i][1]
            val = int(mx[i][2])
            NameByNo[i + 1] = key
            chedaoByName[key] = val
        print(chedaoByName)
        for j in range(2 * n - 2, N):
            if int(mx[j][0]) == 1:
                key = NameByNo[int(mx[j][1])]
                chedaoByName[key] = mx[j][2]
            else:
                key = mx[j][1] + mx[j][2]
                if key in chedaoByName:  # 此处应该用图的遍历算法 ， 可惜没时间了
                    print(chedaoByName.get(key))
                else:
                    print(0)

if __name__ == '__main__':
    solution = Solution()
    n1, n2 = map(int, input().strip().split())
    N = 2 * n1 - 2 + n2
    mx = []
    for _ in range(N):
        string = input().strip()
        lineList = string.split()
        mx.append(lineList)
    solution.minLen(mx, n1, n2)