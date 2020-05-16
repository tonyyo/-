class Solution:
    def findLadders(self, start, end, dict, ans, results):
        if self.canChange(start, end):
            if not results or len(ans) + 1 <= len(results[-1]): # 求最短长度路径
                results.append(ans[:] + [end])
            return
        for i in range(len(dict)):
            if not self.canChange(start, dict[i]):
                continue
            else:
                x = dict[i]
                dict.remove(x)  # 删掉第i个元素
                ans.append(x)
                self.findLadders(x, end, dict, ans, results)
                ans.pop()
                dict.insert(i, x)  # 将第i个元素插回原位置

    def canChange(self, string1, string2): # 相差一个字母返回True
        if len(string1) != len(string2):
            return False
        count = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                count += 1
        if count == 1:
            return True
        else:
            return False
# 主函数
if __name__ == '__main__':
    start = "hit"
    end = "cog"
    dict = ["hot", "dot", "dog", "lot", "log"]
    print("start是：", start)
    print("end是：", end)
    print("dict是：", dict)
    solution = Solution()
    ans = [start]
    results = []
    solution.findLadders(start, end, dict, ans, results)
    print(results)


