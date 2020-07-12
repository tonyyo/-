class Solution:
    def replaceElements(self, arr: [int]) -> [int]:
        N = len(arr)
        result = [0] * N
        result[-1] = -1
        for i in range(N - 2, -1, -1):
            result[i] = max(result[i + 1], arr[i + 1])
        return result