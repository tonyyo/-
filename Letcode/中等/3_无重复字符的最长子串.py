class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N, maxLen = len(s), 0
        import collections
        queue = collections.deque()
        for i in range(N):
            while s[i] in queue: # 得等到队列中不重复，再添加
                queue.popleft()
            queue.append(s[i])
            maxLen = max(maxLen, len(queue))
        return maxLen

if __name__ == '__main__':
    solution = Solution()
    s = "dvdf"
    print(solution.lengthOfLongestSubstring(s))