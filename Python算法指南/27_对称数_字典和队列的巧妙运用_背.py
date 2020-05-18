import collections


class Solution:
    def findStrobogrammatic(self, n):
        Rotate = {}
        Rotate["0"] = "0"
        Rotate["1"] = "1"
        Rotate["6"] = "9"
        Rotate["8"] = "8"
        Rotate["9"] = "6"
        queue = collections.deque()
        if n % 2 == 0:
            queue.append("")
        else:
            queue.append("0")
            queue.append("1")
            queue.append("8")
        while queue:
            temp = queue.popleft()
            if len(temp) == n:
                queue.appendleft(temp)
                break
            for key, val in Rotate.items():
                queue.append(key + temp + val)
        result = []
        for x in queue:
            if x[0] != '0':
                result.append(x)
        return result

if __name__ == '__main__':
    n = 4
    solution = Solution()
    print(solution.findStrobogrammatic(n))
