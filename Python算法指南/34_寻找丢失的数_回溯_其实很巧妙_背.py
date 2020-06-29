class Solution:
    def findMissing2(self, n, str):
        used = [False for _ in range(n + 1)]
        return self.find(n, str, used)

    def find(self, n, str, used):  # 从index处开始找丢失的整数
        result = []
        if str == "":
            for i in range(1, n + 1):
                if not used[i]:
                    result.append(i)
            return result[0] if len(result) == 1 else -1  # 找到后，返回target
        if str[0] == '0':
            return -1  # 为0时直接回溯
        for i in range(1, 3):
            num = int(str[:i])
            if not (1 <= num <= n) or used[num]:
                continue
            used[num] = True
            target = self.find(n, str[i:], used)
            if target != -1:
                return target
            used[num] = False
        return -1# 两种长度的字符串都不满足回溯


# 主函数
if __name__ == '__main__':
    n = 20
    str = "19201234567891011121314151618"
    print("n = ", n)
    print("str = ", str)
    solution = Solution()
    print("缺少的数字是：", solution.findMissing2(n, str))


class Solution:
    def findMissing2(self, n, str):
        used = [False for _ in range(n + 1)]
        return self.find(n, str, 0, used)

    def find(self, n, str, index, used):  # 从index处开始找丢失的整数
        if index == len(str):  # 出口
            results = []
            for i in range(1, n + 1):
                if not used[i]:
                    results.append(i)
            return results[0] if len(results) == 1 else -1
        if str[index] == '0':  # 1-n 里没有0这个数, 如果有, 说明找错了, 需回溯
            return -1
        for l in range(1, 3):  # 因为这里的数只可能是一位或者两位, 所以range是1/2
            num = int(str[index: index + l])
            if num >= 1 and num <= n and not used[num]:  # num需在1-n范围内, 且num不能重复置used为true
                used[num] = True
                target = self.find(n, str, index + l, used)  # 找到了其中的一个数, 继续深度遍历
                if target != -1:  # 这里才是回溯的出口, 直到符合规范, target不等于-1为止
                    return target
                used[num] = False  # 说明不符合规范, target == -1, 需回溯, 举一个简单的例子, 刚开始1可, 但92不可, 回溯到19就可
        return -1
