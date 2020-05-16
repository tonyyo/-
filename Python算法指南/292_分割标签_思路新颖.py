class Solution(object):
    def partitionLabels1(self, S):
        last = {c: i for i, c in enumerate(S)}
        right = left = 0
        ans = []
        for i, c in enumerate(S):
            right = max(right, last[c])
            if i == right:
                ans.append(i - left + 1)
                left = i + 1
        return ans

    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        max_index = 0
        ans = []
        for i, c in enumerate(S):
            max_index = max(max_index, last[c])
            if i == max_index:
                if len(ans) == 0:
                    ans.append(i + 1)
                else:
                    temp = i
                    for x in ans:
                        temp = temp - x
                    ans.append(temp + 1)
        return ans



if __name__ == '__main__':
    temp = Solution()
    string1 = "ababcbacadefegdehijhklij"
    print(("输出：" + str(temp.partitionLabels(string1))))
