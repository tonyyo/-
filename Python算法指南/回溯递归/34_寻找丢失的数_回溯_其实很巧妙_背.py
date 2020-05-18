class Solution:
    def findMissing2(self, n, str):
        used = [False for _ in range(n + 1)]
        return self.find(n, str, 0, used)

    def find(self, n, str, index, used):  # 从index处开始找丢失的整数
        result = []
        if index >= len(str):  # 到了尾部，注意这里不是n
            for i in range(1, len(used)):
                if used[i] == False:
                    result.append(i)
            return result if len(result) == 1 else -1
        for i in range(1, 3):
            temp = int(str[index : index + i])
            if temp == 0:
                return # 如果有0出现， 那么直接返回就好
            elif temp > n:
                continue
            elif used[temp] == True:
                continue
            else:
                used[temp] = True
                result= self.find(n, str, index + i, used)
                used[temp] = False
        return result

# 主函数
if __name__ == '__main__':
    n = 20
    str = "19201234567891011121314151618"
    print("n = ", n)
    print("str = ", str)
    solution = Solution()
    print("缺少的数字是：", solution.findMissing2(n, str))