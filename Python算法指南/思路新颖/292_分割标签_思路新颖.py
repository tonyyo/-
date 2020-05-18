class Solution(object):
    def partitionLabels1(self, S):
        last = {c: i for i, c in enumerate(S)}
        right = left = 0  # right永远指向前i个字母中最大的索引标签， left中是前i个字母的起步。
        ans = []
        for i, c in enumerate(S):
            right = max(right, last[c])
            if i == right:
                ans.append(i - left + 1)
                left = i + 1
        return ans

    def partitionLabels(self, S):
        Last = {v : k for k, v in enumerate(S)}  # 记录每个字母出现的最大索引位置
        left = right = 0   # 左边记录着该部分的开头，right记录着该部分的结尾
        ans = []  # 记录每个部分的长度
        for i in range(len(S)):
            right = max(right, Last[S[i]])
            if right == i:
                ans.append(right - left + 1)
                left = i + 1
        return ans

if __name__ == '__main__':
    temp = Solution()
    string1 = "ababcbacadefegdehijhklij"
    print(("输出：" + str(temp.partitionLabels(string1))))
