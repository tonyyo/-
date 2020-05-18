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
        tempQueue1 = collections.deque()
        tempQueue2 = collections.deque()
        result = []
        for j in range(size):
            tempQueue1.append(gas[j])
            tempQueue2.append(cost[j])
        for i in range(size):
            queue1, queue2 = tempQueue1.copy(), tempQueue2.copy()
            flag = True
            for _ in range(i):
                temp1 = queue1.popleft()
                temp2 = queue2.popleft()
                queue1.append(temp1)
                queue2.append(temp2)
            carOil = 0
            for j in range(len(gas) - 1):
                carOil += queue1[j] - queue2[j]
                if carOil < 0:
                    flag = False
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