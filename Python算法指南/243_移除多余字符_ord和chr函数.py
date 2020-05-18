class Solution:
    def removeDuplicateLetters1(self, s):
        vis, num = [False] * 26, [0] * 26;
        S, cnt = [0] * 30, 0
        for c in s:
            num[ord(c) - ord('a')] += 1  # ord将字符转化为ASII数字, chr将数字转化为ASII字符
        for c in s:
            id = ord(c) - ord('a')
            num[id] -= 1
            if (vis[id]):
                continue
            while cnt > 0 and S[cnt - 1] > id and num[S[cnt - 1]] > 0:
                vis[S[cnt - 1]] = False
                cnt -= 1
            S[cnt] = id
            cnt += 1
            vis[id] = True
        ans = ""
        for i in range(cnt):
            ans += chr(ord('a') + S[i])
        return ans

    def removeDuplicateLetters(self, s):
        listS = list(s)
        setS = set(listS)
        tempS = ''.join(x for x in setS)
        return tempS
#主函数
if __name__ == "__main__":
    s = "bcabc"
    s2 = "cbacdcbc"
    #创建对象
    solution = Solution()
    print("移除多余字符后的结果是：", solution.removeDuplicateLetters(s))
    print("移除多余字符后的结果是：", solution.removeDuplicateLetters(s2))