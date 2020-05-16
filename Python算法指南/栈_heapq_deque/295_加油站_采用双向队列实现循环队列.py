import collections


class Solution:
    def canCompleteCircuit1(self, gas, cost):
        n = len(gas)
        diff = []
        for i in range(n): diff.append(gas[i]-cost[i])
        for i in range(n): diff.append(gas[i]-cost[i])
        if n==1:
            if diff[0]>=0: return 0
            else: return -1
        st = 0
        now = 1
        tot = diff[0]
        while st<n:
            while tot<0:
                st = now
                now += 1
                tot = diff[st]
                if st>n: return -1
            while now!=st+n and tot>=0:
                tot += diff[now]
                now += 1
            if now==st+n and tot>=0: return st
        return -1

    def canCompleteCircuit(self, gas, cost):
        size = len(gas)
        result = []
        for i in range(size):
            gasQueue = collections.deque(gas)
            costQueue = collections.deque(cost)
            flag = True  # 刚开始假设都能通过
            for _ in range(i):  # 制作以第i个元素开头的队列
                temp1 = gasQueue.popleft()
                temp2 = costQueue.popleft()
                gasQueue.append(temp1)
                costQueue.append(temp2)
            carOil = 0
            for j in range(len(gas) - 1):
                carOil += gasQueue[j] - costQueue[j]
                if carOil < 0:
                    flag = False  # 油不够，置为False
                    break
            if flag:
                result.append(i)
        return result

if __name__ == '__main__':
    temp = Solution()
    List1 = [1, 1, 3, 1]
    List2 = [2, 2, 1, 1]
    print(("输入："+str(List1)+"  "+str(List2)))
    print(("输出："+str(temp.canCompleteCircuit(List1,List2))))