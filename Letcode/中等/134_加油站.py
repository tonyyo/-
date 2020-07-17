class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        N = len(gas)
        for i in range(N): # 起始点
            gasSum = 0
            for j in range(N):
                pos = (i + j) % N # 遍历点
                gasSum += gas[pos] - cost[pos]
                if gasSum < 0:
                    break
            if gasSum >= 0:
                return i
        return -1
if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    solution = Solution()
    print(solution.canCompleteCircuit(gas, cost))