class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N, maxLen = len(s), 0
        import collections
        queue = collections.deque()
        queue.append(0)
        j = 0   # 全局末尾指针
        for i in range(N):
            queue.popleft()
            while j < N and s[j] not in queue:
                queue.append(s[j])
                j += 1
            maxLen = max(maxLen, len(queue))
        return maxLen
if __name__ == '__main__':
    solution = Solution()
    s = "dvdf"
    print(solution.lengthOfLongestSubstring(s))